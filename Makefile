install:
	pip install -r requirements.txt
	python src/app/set_database.py

run:
	python src/main.py

uninstall:
	rm datasets/plants.db