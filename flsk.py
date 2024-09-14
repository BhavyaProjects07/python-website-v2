from flask import Flask,render_template
from flask import jsonify
from database import get_db_connection
import os
app = Flask(__name__,static_folder='static')
Picfolder = os.path.join('static','images')
app.config['UPLOAD_FOLDER'] = Picfolder




def load_jobs_from_db():
    jobs = []
    connection = get_db_connection()  # Open a new connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM jobs")
            result = cursor.fetchall()
            for i in result:
                jobs.append(i)
    finally:
        connection.close()  # Close the connection after the query
    return jobs



@app.route('/')
def hello_world():
    jobs = load_jobs_from_db()
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'football.jpeg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'logo.svg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'],'people.jpeg')
    return render_template('web.html',jobs = jobs,company_name='ALL',user_image = pic1,user_image2 = pic2,user_image3 = pic3)


@app.route("/jobs")
def list_jobs():
    return jsonify(list_jobs)

if __name__ == '__main__':
    app.run(debug=True)


