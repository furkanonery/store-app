FROM python:3.10.12

WORKDIR /app

COPY .gitignore LICENSE README.md .env requirements.txt core /app/

RUN pip3 install --upgrade pip

RUN pip3 install -r "requirements.txt"

COPY . /app/

RUN cd core

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]