FROM python:3.8-alpine3.15

WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]