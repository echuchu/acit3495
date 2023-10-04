FROM python

# Flask Applications listen to port 5000 by default
# Expose it
EXPOSE 5000

# Working Directory 
# Creates a directory with this name if it does not exist
WORKDIR /web_upload

# Install any needed packages specified in the requirements.txt
COPY requirements.txt /web_upload/
RUN pip install -r requirements.txt

# Run app.py when the container launches
COPY app.py /web_upload/
CMD ["python", "app.py"]