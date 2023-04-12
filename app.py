# app.py file

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
     name = "Brandon Gonzalez"
     details = readDetails('static/details.txt')
     return render_template("homepage.html", name=name, aboutMe=details)

def readDetails(filepath):
     with open (filepath, 'r') as f:
          return [line for line in f]
     
def writeToFile(filename, message):
     with open(filename, 'a') as f:
          f.write(message)


@app.route('/form', methods=['GET', 'POST'])
def formDemo():
     #need a variable name in order to pass as context in render template
     name = None
     if request.method == 'POST':
          name = request.form['name']
          # if request.form['message']:
          #      writeToFile('/static/comments.txt', request.form['message'])
          
     return render_template('form.html', name=name)

@app.route("/coolpage")
def coolpage():
     # return f"<h1>Hi there, {name}!</h1>"
     return render_template('coolpage.html')

if __name__ == "__main__":
     app.run(debug=True, port=2000)