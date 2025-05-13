

FROM python:3.12-alpine


WORKDIR /app

COPY FictionalIceParlour/ 

CMD ["python", "main.py"]
