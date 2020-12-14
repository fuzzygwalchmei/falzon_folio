<<<<<<< HEAD
from flask import Flask, render_template, redirect, url_for

from views.education import education_blueprint
from views.gaming import gaming_blueprint
from views.blog import blog_blueprint



app = Flask(__name__)
app.config['SECRET_KEY']='you_will_never_know'

app.register_blueprint(education_blueprint, url_prefix="/education")
app.register_blueprint(gaming_blueprint, url_prefix="/gaming")
app.register_blueprint(blog_blueprint, url_prefix="/blog")

@app.route("/")
def index():
    return render_template("home.html")

=======
from webApp import app

app.run(debug=True)
>>>>>>> e90050dedbe67d0656b976b8c63d97363b16d7ec
