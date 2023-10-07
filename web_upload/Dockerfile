FROM python:3.9

# Flask Applications listen to port 5000 by default
# Expose it
EXPOSE 5000

# Working Directory 
# Creates a directory with this name if it does not exist
WORKDIR /web_upload

# Install any needed packages specified in the requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run app.py when the container launches
CMD ["python", "app.py"]