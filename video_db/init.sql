CREATE DATABASE video;

USE video;

CREATE USER 'video_user'@'%' IDENTIFIED BY 'password';

GRANT SELECT, INSERT, UPDATE ON video.* TO video_user;

CREATE TABLE video_files (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255),
    filepath VARCHAR(255)
)