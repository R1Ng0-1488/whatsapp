from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings

import base64
import time
import requests

from main.models import Chat


url = 'https://dev.wapp.im/v3/'
headers = {'X-Tasktest-Token': 'f62cdf1e83bc324ba23aee3b113c6249'}


def get_number(ID, TOKEN):
    path = 'instance{ID}/getNUmberId?token={TOKEN}&phone=89872745052'
    r = requests.get(url + path, headers=headers)
    print(r.json())

def send_message(ID, TOKEN):
    path = 'instance{ID}/sendMessage?token={TOKEN}'
    data = {
        'phone': '89872745052',
        # 'phone': '89587629719',
        'body': 'Артём +79225438051',
    }
    r = requests.post(url + path, data=data, headers=headers)
    print(r.json())

def initialte_chat(ID, TOKEN):
    METHOD = 'status'
    path = f'instance{ID}/{METHOD}?full=1&token={TOKEN}'
    r = requests.get(url + path, headers=headers)
    print(r.json())
    return r.json()

def get_chat():
    path = 'chat/spare?crm=TEST&domain=test'
    r = requests.get(url + path, headers=headers)
    data = r.json()
    print(data)
    return data

def save_qr(data):
    imgdata = base64.b64decode(data.split(',')[1])
    file = settings.MEDIA_ROOT / 'qr.jpg'
    with open(file, 'wb') as f:
        f.write(imgdata)

class Command(BaseCommand):
    help = "get qr"

    def handle(self, *args, **options):
        try:
            response = get_chat()
            if response.get('id'):
                chat = Chat(**response)
                chat.save()
            else:
                chat = Chat.objects.first()
            while True:
                response = initialte_chat(chat.id, chat.token)
                if response.get('state') == 'got qr code':
                    qr_code = response.get('qrCode')
                    save_qr(qr_code)
                    
                if response.get('state') == 'CONNECTED':
                    send_message(chat.id, chat.token)
                        
                time.sleep(60)
        except Exception as e:
            print(e)