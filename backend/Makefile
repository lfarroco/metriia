dev:
	pip install --no-cache-dir -r requirements.txt
	python ./src/manage.py migrate
	python ./src/manage.py runserver 0.0.0.0:8000

migrations:
	python ./src/manage.py makemigrations

migrate:
	python ./src/manage.py migrate

flush:
	rm -rf ./src/db.sqlite3
	python ./src/manage.py migrate

shell:
	python ./src/manage.py shell

freeze:
	pip freeze > requirements.txt

ingest:
	python ./src/manage.py ingest cs.SE
	python ./src/manage.py calc_embeddings
	python ./src/manage.py calc_embeddings_distance