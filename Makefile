runserver:
	python3 server/manage.py runserver

migrate:
	python3 server/manage.py migrate

makemigrations:
	python3 server/manage.py makemigrations

createsuperuser:
	python3 server/manage.py createsuperuser

startapp:
	python3 server/manage.py startapp $(app_name)
