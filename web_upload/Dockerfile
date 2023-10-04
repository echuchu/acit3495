FROM python

# Flask Applications listen to port 5000 by default
# Expose it
EXPOSE 5000

# Working Directory 
# Creates a directory with this name if it does not exist
WORKDIR /app_upload

# Install any needed packages specified in the requirements.txt
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Run app.py when the container launches
COPY app_upload.py /app_upload//
CMD ["python", "app_upload.py"]