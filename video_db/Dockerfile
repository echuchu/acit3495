FROM mysql:8.0

# environment variables
# ENV MYSQL_ROOT_PASSWORD=root_password
# ENV MYSQL_DATABASE=video
# ENV MYSQL_USER=video_user
# ENV MYSQL_PASSWORD=password

# SQL script to initialize database
COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
