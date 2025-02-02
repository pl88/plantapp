FROM python:3.12

#workdir
WORKDIR /plantapp

COPY ./requirements.txt /plantapp/requirements.txt

COPY ./alembic.ini /plantapp/alembic.ini

RUN pip install --no-cache-dir --upgrade -r /plantapp/requirements.txt

ENV PYTHONPATH=/plantapp/plantapp/
#execute command
# CMD ["uvicorn", "plantapp.main:app", "--host", "0.0.0.0", "--port", "8000"]