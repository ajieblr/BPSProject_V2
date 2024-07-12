from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/predict')
def page1():
    return render_template('predict.html')

@app.route('/profile')
def page2():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
    