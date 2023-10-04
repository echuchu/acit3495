import os
import yaml
from flask import *
from base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from video_file import VideoFile
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Reading credentials
with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

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

# Create the "videos" folder if it doesn't exist
if not os.path.exists('videos'):
    os.makedirs('videos')


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
            filepath = os.path.abspath(os.path.join('videos', filename))

            # Save the file to the "videos" folder
            f.save(filepath)

            # Insert file information into the database
            session = DB_SESSION()
            video = VideoFile(filename=filename, filepath=filepath)

            session.add(video)
            session.commit()
            session.close()

            return render_template("Success.html", name=filename)
        else:
            return "Invalid file format. Please upload a valid video file."

if __name__ == '__main__':
    app.run(debug=True)
