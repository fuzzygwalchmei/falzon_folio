from flask import Blueprint, render_template

home_blueprint = Blueprint('home', __name__)

page_config = {"colour": "#AF3731", "icon": "blog.png", "title": "Falzon Folio: Home", "links": {
    "about": "https://google.com", "personal": "https://google.com"}}

@blog_blueprint.route('/')
def index():
    return render_template('home/index.html', page_config=page_config)