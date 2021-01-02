from flask import Flask

from .views.education import education_blueprint
from .views.gaming import gaming_blueprint
from .views.blog import blog_blueprint
from .views.home import home_blueprint
from .views.api import api_bp

from dotenv import load_dotenv
import os
load_dotenv()



app = Flask(__name__)
app.config['SECRET_KEY']=os.environ.get('secret_key')

app.register_blueprint(home_blueprint, url_prefix="/home")
app.register_blueprint(education_blueprint, url_prefix="/education")
app.register_blueprint(gaming_blueprint, url_prefix="/gaming")
app.register_blueprint(blog_blueprint, url_prefix="/blog")
app.register_blueprint(api_bp, url_prefix="/api")
