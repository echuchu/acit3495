import yaml
import pymysql

from flask import *
from base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from video_file import VideoFile
from werkzeug.utils import secure_filename
from ftplib import FTP

container_ip = 'filesys'
ftp_port = 20
ftp_username= 'user'
# ftp_password = ''


app = Flask(__name__)


# Reading credentials
with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

# ftp = FTP()

# ftp.connect(host='x', port=)
# print(ftp.getwelcome())
# ftp.login(user='ftp')

# FTP.connect(app_config["fileupload"]["host"], app_config["fileupload"]["port"])
# FTP.login(user=app_config["fileupload"]["user"], passwd=app_config["fileupload"]["password"])


# Create and connect to the database
DB_ENGINE = create_engine(f'mysql+pymysql://'
                          f'{app_config["datastore"]["user"]}:'
                          f'{app_config["datastore"]["password"]}@'
                          f'{app_config["datastore"]["hostname"]}:'
                          f'{app_config["datastore"]["port"]}/'
                          f'{app_config["datastore"]["db"]}')
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'wmv'}
DIRECTORY = '~/static'


# Function to check if a filename has a valid video file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Page to upload video files
@app.route('/upload')
def upload():
    return render_template("Upload.html")

# Successfully uploading video files
@app.route('/upload_success', methods=['POST'])
def upload_success():
    if request.method == 'POST':
        f = request.files['file']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            filepath = FTP.storbinary(f"STOR {DIRECTORY}/", filename)

            # Insert file information into the database
            session = DB_SESSION()
            video = VideoFile(filename=filename, filepath=filepath)

            session.add(video)
            session.commit()
            session.close()

            return render_template("Success.html", name=filename)
        else:
            # Lead the user here if the upload is invalid
            return render_template("InvalidUpload.html")

if __name__ == '__main__':
    app.run(debug=True)
