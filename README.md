# whatsapp
whatsapp

### To start this app you need to download and install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/)

##### start the project: docker-compose up -d
##### create migrations: docker-compose exec web python manage.py makemigrations
##### execute migrations: docker-compose exec web python manage.py migrate
##### create a superuser: docker-compose exec web python manage.py createsuperuser
##### launch this app: docker-compose exec web python manage.py get_qr

##### all the logic of the code is in main/management/commands/get_qr.py
