install:
	pip install -r requirements.txt && \
	alembic upgrade head

run:
	python src/app/main.py

start_www:
	uvicorn src.app.main:app --host 0.0.0.0 --port 8000

tests:
	cd src/app && pytest -vv

docker_build:
	docker build -t plantapp_img .

docker_run:
	docker container stop plantapp && \
	docker container rm plantapp && \
	docker run -d --name plantapp -p 8888:8888 plantapp_img