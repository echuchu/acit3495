FROM nginx:latest

# for htpasswd command
RUN apt update
RUN apt install -y apache2-utils
RUN rm -f /etc/nginx/conf.d/*

ENV CLIENT_MAX_BODY_SIZE 1m
ENV PROXY_READ_TIMEOUT 60s
ENV WORKER_PROCESSES auto

COPY files/index.html /
COPY files/runfile /
COPY files/nginx.conf.tmpl /

# use SIGQUIT for graceful shutdown
# c.f. http://nginx.org/en/docs/control.html
STOPSIGNAL SIGQUIT

ENTRYPOINT ["/runfile"]