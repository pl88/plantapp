install:
	pip install -r requirements.txt

run:
	python src/app/main.py

start_www:
	uvicorn src.app.main:app --host 0.0.0.0 --port 8000

test:
	cd src && pytest -vv

migrations:
	cd src && alembic revision --autogenerate && alembic upgrade head
