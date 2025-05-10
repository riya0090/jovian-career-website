from flask import Flask, render_template, jsonify
app = Flask(__name__)
JOBS=[{
     'id':'1',
     'title': 'Data Analyst',
     'location': 'Bengaluru,India',
     'salary': 'Rs 10,00,000'
},
{
     'id':'2',
     'title': 'Frontend Engineer',
     'location': 'Delhi,India',
     'salary': 'Rs 15,00,000'
},
{
     'id':'3',
     'title': 'Backend Engineer',
     'location': 'Remote,India',
},
{
     'id':'4',
     'title': 'DataScientist Engineer',
     'location': 'San Fransisco',
     'salary': '$12,0,000'
}
]
@app.route("/")# we are create this route which says that when we go to the home page we want to return the hello world
def hello_world():
     return render_template('home.html', jobs=JOBS, company_name='Jovian')#we are returning the home.html file and we are passing the jobs list also the company name which is dynamic to the home.html file 
@app.route("/api/jobs")
def list_jobs():
     return jsonify(JOBS)
 
if __name__ == "__main__":
     app.run(host= '0.0.0.0', debug=True)
