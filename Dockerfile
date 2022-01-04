FROM python:3.9.5-buster

WORKDIR /root/SpideyRobot 

COPY . .

RUN pip install -r requirements.txt

CMD ["python3","-m","SpideyRobot"]
