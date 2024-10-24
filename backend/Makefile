dev:
	pip install --no-cache-dir -r requirements.txt
	python ./src/manage.py migrate
	python ./src/manage.py runserver 0.0.0.0:8000

makemigrations:
	python ./src/manage.py makemigrations

migrate
	python ./src/manage.py migrate

shell:
	python ./src/manage.py shell

freeze:
	pip freeze > requirements.txt