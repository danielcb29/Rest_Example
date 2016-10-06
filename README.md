# Rest_Example
This is a django rest server and django rest client example. 

To install the proyect follow next instructions 

- Clone 
- Create a python3 virtualenv:
  ->Virtualenv wrapper: mkvirtualenv rest_example
- Install the requeriments (requeriments.txt)
  -> pip install -r requeriments.txt
- Create and configure PSQL database
  -> Database named: eps_server
  -> Database user: eps_server
  -> Database pass: eps_server
- Set EPS initial data
  -> Run eps_server/datos_iniciales/datos_eps.sql in database eps_server
- Run both projects (server in port 8088)
  -> eps_server: python manage.py runserver 8088
  -> eps_client: python manage.py runserver 8087
- Go http://localhost:8087

# By
Daniel Correa 
EISC
Universidad del Valle
