from flask import Blueprint, render_template

blog_blueprint = Blueprint('blog', __name__)

page_config = {"colour": "blue", "icon": "blog.png", "title": "Falzon Folio: Blog", "links": {
    "about": "https://google.com", "personal": "https://google.com"}}

@blog_blueprint.route('/')
def index():
    return render_template('blog/index.html', page_config=page_config)