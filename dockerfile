FROM python:3.8-slim-buster

WORKDIR /archit

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["sh","-c","export FLASK_APP=blockAccount.py && flask run -h localhost -p 8081 && export FLASK_APP=Token.py && flask run -h localhost -p 8080"]
