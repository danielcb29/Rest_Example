# Rest_Example
This is a django rest server and django rest client example. 

To install the proyect follow next instructions 

1. Clone 

2. Create a python3 virtualenv:

	- Virtualenv wrapper: 
	
	```python
	mkvirtualenv rest_example
	```
	
	```python
	workon rest_example
	```

3. Install the requeriments (requeriments.txt)

	- pip install -r requeriments.txt.

4. Create and configure PSQL database

	- Database named: eps_server.

	- Database user: eps_server.

	- Database pass: eps_server.

5. Set EPS initial data

	- Run eps_server/datos_iniciales/datos_eps.sql in database eps_server.

6. Run both projects (server in port 8088)

	- eps_server: 

	```python
		python manage.py runserver 8088
	```
	- eps_client:

	
	```python
		python manage.py runserver 8087
	```

7. Go http://localhost:8087

# By
Daniel Correa 
EISC
Universidad del Valle
