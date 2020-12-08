from flask import render_template, url_for,flash, redirect
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Successfully login!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful login. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
