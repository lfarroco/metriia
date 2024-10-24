build:
	pip install --no-cache-dir -r requirements.txt && \
	python ./src/manage.py migrate && \
	python ./src/manage.py runserver

freeze:
	pip freeze > requirements.txt