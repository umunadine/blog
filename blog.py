from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/quote')
def quote():
    return render_template('quote.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug = True)