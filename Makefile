install:
	pip install -r requirements.txt && \
	alembic upgrade head

run:
	python src/app/main.py

tests:
	docker exec -it plantapp_web pytest

docker_build:
	docker build -t plantapp_img .

docker_run:
	docker container stop plantapp && \
	docker container rm plantapp && \
	docker run -d --name plantapp -p 8888:8888 plantapp_img
