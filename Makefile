install:
	pip install -r requirements.txt

run:
	python src/app/main.py

start_www:
	uvicorn src.app.main:app --host 0.0.0.0 --port 8000

docker_build:
	docker build -t plantapp_img .

docker_run:
	docker run -d --name plantapp -p 8888:8888 plantapp_img