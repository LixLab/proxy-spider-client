FROM python:3
COPY . /opt/app
COPY .env.example /opt/app/.env
WORKDIR /opt/app
RUN pip install -r requirements.txt
CMD [ "python", "index.py" ]