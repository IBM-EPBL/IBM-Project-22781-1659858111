FROM ubuntu:latest


WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN apt update
RUN apt install -y python3-pip
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
