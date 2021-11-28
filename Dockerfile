FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apk update && apk add gcc librdkafka-dev openssl-libs-static zlib-static zstd-libs libsasl librdkafka-static lz4-dev lz4-static zstd-static libc-dev musl-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]