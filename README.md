
# django-real-estate

A simple real estate app, built with React, Redux, Ngnix, Docker and more.. 

<b>Used in project:</b>

-POSTMAN 

-djoser

-JWTAuthentication

-SendGrid

-flower

-celery

-redis



## Flower
 PORT: 5557, Is a real time web application for monitoring and administration tasks in celery
 
 
## TESTS: 
 -  pytest -p no:warnings --cov=. --cov-report html



<b>Configured</b>:

 -gitignore
	
-venv
 
 -split settings(base, development, production)
 
 -requirements.txt
 
 -logging.conf (save logs into the file)
 
 -"profile.exceptions"
 
	
	

 <b>Building APIs with Django REST framework:</b>

• Custom user models and model managers in Django.

• Token based authentication.

• UUID’s (advantages and disadvantages) and how pseudo primary keys solve this.

• Intro to Python and Django API testing with Pytest using factories and fixtures.

• Python Test coverage 

• Django filtering.

• Django signals

• Django admin customization

• Django security.

• Logging in Django.

• Docker and containers with docker-compose.

• shell scripts in Docker

• Asynchronous tasks with Celery and Redis

• Asynchronous tasks monitoring with Flower

• Working with Postgres within a Docker container 

• Setting up Nginx as a web server /reverse proxy.

• Serving static and media files with Nginx

• Utilizing Makefiles to make working with Docker easier.

• React Hooks.

• Redux.

• Using Ant Design with React

### MAKEFILE - shorts for commands

- make build
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



