FROM python:3.7-alpine

RUN adduser -D arthur

WORKDIR /home/arthur

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
#COPY migrations migrations
COPY main.py config.py #boot.sh ./
#RUN chmod +x boot.sh

ENV FLASK_APP main.py

RUN chown -R arthur:arthur ./
USER arthur

EXPOSE 5000
ENTRYPOINT ["gunicorn -b :5000 --access-logfile - --error-logfile - main:app"]
