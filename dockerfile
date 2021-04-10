FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /archit

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["sh","-c","export FLASK_APP=Main.py && flask run -h localhost -p 8080"]
