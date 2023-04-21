
# django-real-estate



<b>Building APIs with Django REST framework:</b>

• Custom user models and model managers in Django.

• Token based authentication.

• UUID

• Python Test coverage 

• Django filtering

• Django signals

• Django admin customization

• Django security

• Logging in Django

• Docker and containers with docker-compose

• shell scripts in Docker

• Asynchronous tasks with Celery and Redis

• Asynchronous tasks monitoring with Flower

• Working with Postgres within a Docker container 

• Setting up Nginx as a web server /reverse proxy

• Serving static and media files with Nginx

• Utilizing Makefiles to make working with Docker easier

• React Hooks

• Redux

• Postman


## CELERY
- Sendign email with celery : https://pypi.org/project/django-celery-email/

## Flower
 PORT: 5557, Is a real time web application for monitoring and administration tasks in celery
 
## TESTS: 
 -  pytest -p no:warnings --cov=. --cov-report html



<b>Configured</b>:

 -gitignore
	
 -venv
 
 -split settings(base, development, production)
 
 -each model in different app
 
 -requirements.txt
 
 -logging.conf (save logs into the file)
 


### MAKEFILE - shorts for commands

- make build
- make up - run container
- make volume - check if postgres is ready
- make superuser 
- make estate-db - login to database
 	- \list -list of databases
 	- \connect - connect to db
 	- \q - quit
 

### DOCKER
-  sudo kill -kill $(sudo lsof -t -i :5432)
-  docker config
-  docker compose up --build -d --remove-orphans
-  docker compose down
-  docker ps – container list 
-  docker exec -it {id} bash  - enter to container terminal
-  docker-compose build {nazwa kontenera}  - rebuild container



