# Use the official Ubuntu 20.04 image as the base image
FROM ubuntu:20.04

# Update package lists and install vsftpd
RUN apt-get update && \
    apt-get install -y vsftpd

# Create the chroot directory as specified in vsftpd.conf
RUN mkdir -p /var/run/vsftpd/empty

# Copy the vsftpd configuration file to the container
COPY vsftpd.conf /etc/vsftpd.conf

# Expose FTP ports (20 for data transfer, 21 for control)
EXPOSE 20 21

# Create a directory for the FTP data
RUN mkdir -p /srv/ftp/shared

# Set permissions for the FTP directory
RUN chmod 755 /srv/ftp
RUN chmod 777 /srv/ftp/shared

# Run vsftpd in the foreground when the container starts
CMD ["vsftpd", "/etc/vsftpd.conf"]