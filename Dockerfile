FROM python:3.8

RUN pip install pipenv

WORKDIR /code

COPY Pipfile* ./

RUN pipenv install --system

COPY . .

CMD [ "python", "./ssl-checker.py", "check-all-ssl" ]
