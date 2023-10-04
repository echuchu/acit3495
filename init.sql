CREATE DATABASE video;

USE video;

CREATE USER 'video_read_write'@'%' IDENTIFIED BY 'password';



CREATE TABLE video_files (
    id UNIQUEIDENTIFIER PRIMARY KEY,
    filename VARCHAR(255),
    filepath VARCHAR(255)
)