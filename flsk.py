from flask import Flask,render_template
from flask import jsonify
import os
app = Flask(__name__,static_folder='static')
Picfolder = os.path.join('static','images')
app.config['UPLOAD_FOLDER'] = Picfolder
JOBS = [

    
    {
        'Id': 1,
        'Title' : 'Data Anaylist',
        'Location' : 'Philedelphia , USA',
        'Salary' : '$1,20,000'
    },
    {
        'Id': 2,
        'Title' : 'Web Devloper',
        'Location' : 'California , USA',
        'Salary' : '$1,00,000'
    },
    {
        'Id': 3,
        'Title' : 'App Devloper',
        'Location' : 'Bengaluru , India',
        'Salary' : '$1,50,000'
    },
    {
        'Id': 4,
        'Title' : 'FrontEnd Engineer',
        'Location' : 'Dallas , Texas',
        'Salary' : '$84599'
    }
]


@app.route('/')
def hello_world():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'football.jpeg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'logo.svg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'],'people.jpeg')
    return render_template('web.html',jobs = JOBS,company_name='ALL',user_image = pic1,user_image2 = pic2,user_image3 = pic3)


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)


