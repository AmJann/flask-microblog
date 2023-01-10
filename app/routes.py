from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Amber'}
    posts = [
        {
            'author': {'username': 'Mike'},
            'body': 'Beautiful day in Florida'
        },
        {
            'author': {'username': 'Jane'},
            'body': 'Went to the movies today!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
 
