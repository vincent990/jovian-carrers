from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data analyst',
    'location':'Severin, Romania',
    'Salary':'Ron 10000'
  },
  {
    'id':2,
    'title':'Frontend',
    'location':'Bucharest, Romania',
    'Salary':'Ron 12000'
  },
  {
    'id':3,
    'title':'Backend',
    'location':'Timisoara, Romania',
    'Salary':'Ron 20000'
  },
  {
    'id':4,
    'title':'Engineer',
    'location':'Cluj, Romania',
    'Salary':'Ron '
  },
]

@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
