FROM python:3.7-alpine

RUN adduser -D arthur

WORKDIR /home/arthur

COPY requirements.txt requirements.txt
RUN apk update && apk add zlib-dev libzip-dev build-base \
                       python-dev python3-dev \
                         # Pillow dependencies
                       jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev
RUN pip install -r requirements.txt

COPY app app
#COPY migrations migrations
#RUN chmod +x boot.sh
WORKDIR /home/arthur/app
ENV FLASK_APP main.py
ENV S3BUCKET "s3://none"

RUN chown -R arthur:arthur ./
USER arthur

EXPOSE 5000
ENTRYPOINT ["/usr/local/bin/gunicorn","-b :5000", "--access-logfile", "-", "--error-logfile",  "-", "main:app"]
