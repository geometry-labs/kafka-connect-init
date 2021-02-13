FROM python:3.6 as base
ENV PROJECT_DIR=src

RUN mkdir /$PROJECT_DIR
WORKDIR /$PROJECT_DIR
COPY . .
RUN pip install --upgrade pip && pip install -r /$PROJECT_DIR/requirements.txt

ENTRYPOINT ["python", "main.py"]

