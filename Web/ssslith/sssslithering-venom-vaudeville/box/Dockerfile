FROM golang AS builder

COPY app /src
WORKDIR /src
RUN go mod init example.com/app
RUN go get github.com/google/uuid
RUN go build -o app app.go 

FROM ubuntu:latest

RUN apt-get update && apt-get install -y gawk ncat telnet sudo

RUN mkdir /app
WORKDIR /app
RUN mkdir log

COPY app/ .
# RUN rm -rf src
COPY --from=builder /src/app .
COPY entrypoint.sh /

RUN touch log/master_logfile.log
RUN touch log/warning_logfile.log

RUN useradd -m user
RUN chown user:user log/warning_logfile.log log/master_logfile.log

ENV PORT=80
EXPOSE 80

CMD ["/entrypoint.sh"]
