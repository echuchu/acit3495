from distutils.log import debug
from fileinput import filename
import mysql.connector
from flask import *

app = Flask(__name__)

# credentials = {
#         'user': 'video_user',
#         'password': 'video_password',
#         'host': 'mysql',
#         'port': '3306',
#         'database': 'video_database'
#     }

# connection = mysql.connector.connect(**credentials)

@app.route('/')
def main():
    return render_template("./templates/index.html")

@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template("./templates/Acknowledgement.html", name = f.filename)  
  
if __name__ == '__main__':  
    app.run(debug=True)