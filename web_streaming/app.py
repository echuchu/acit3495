import yaml
import pymysql

from flask import *
from base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from video_file import VideoFile
from ftplib import FTP

app = Flask(__name__)
app.static_folder = '/tmp'


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

# Page to display video files
@app.route('/display')
def display():
    # Fetch video data from the database
    session = DB_SESSION()
    video_files = session.query(VideoFile).all()
    session.close()

    return render_template("VideoPlayer.html", video_files=video_files)


@app.route('/play_video/<int:video_id>')
def play_video(video_id):
    session = DB_SESSION()
    selected_video = session.query(VideoFile).filter_by(id=video_id).first()
    session.close()

    ftp = FTP('filesys')
    ftp.login()

    with open(f'/tmp/{selected_video.filename}', 'wb') as f:
                ftp.retrbinary(f'RETR {selected_video.filepath}', f.write)
    
    ftp.quit()

    if selected_video:
        # Construct the full path to the video file based on the database filepath
        return render_template("VideoPlayer.html", 
                               video_path=selected_video.filepath, 
                               video_name=selected_video.filename)
    else:
        return "Video not found"




if __name__ == '__main__':
    app.run(host='0.0.0.0')
