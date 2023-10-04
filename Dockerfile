FROM mysql

# environment variables
ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=video_database
ENV MYSQL_USER=video_user
ENV MYSQL_PASSWORD=video_password

# SQL script to initialize the database?
COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
 