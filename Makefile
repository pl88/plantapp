install:
	pip install -r requirements.txt && \
	alembic upgrade head

run:
	python src/app/main.py

start_www:
	uvicorn src.app.main:app --host 0.0.0.0 --port 8000

