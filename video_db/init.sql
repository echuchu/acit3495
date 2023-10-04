CREATE DATABASE video;

USE video;

CREATE USER 'video_read_write'@'%' IDENTIFIED BY 'password';

GRANT SELECT, INSERT, UPDATE ON video.* TO video_read_write;

CREATE USER 'video_read_only'@'%' IDENTIFIED BY 'password';

GRANT SELECT ON video.* TO video_read_only;

CREATE TABLE video_files (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255),
    filepath VARCHAR(255)
)