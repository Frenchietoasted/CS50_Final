from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('layout.html')

@app.route('/search', methods=['GET', 'POST'])    
def search():
    return render_template('search.html')
