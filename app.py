from flask import Flask, render_template, jsonify

app =Flask(__name__)


JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru, India',
        'salary':'Rs. 10,00,000'
    },
    {
        'id':2,
        'title':'Data sientist',
        'location':'algeirs, algeria',
        'salary':'$ 20,00,000'
    },
    {
        'id':3,
        'title':'backtend engineer',
        'location':'london, britan',
        'salary':'$ 15,00,000'
    },
    {
        'id':4,
        'title':'frontend engineer',
        'location':'online',
        'salary':'$ 12,00,000'
    }
]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs = JOBS, company_name='DiDa')

@app.route("/jobs")
def list_jobs():
    return jsonify (JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)
   