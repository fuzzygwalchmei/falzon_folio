from flask import Blueprint, render_template

blog_blueprint = Blueprint('blog', __name__)

page_config = {"colour": "#4080BF", "icon": "blog.png", "title": "Falzon Folio: Blog", "links": {
    "about": "#", "personal": "#"}}


@blog_blueprint.route('/')
def index():
    return render_template('blog/index.html', page_config=page_config)


@blog_blueprint.route('/about')
def about():
    return render_template('blog/about.html', page_config=page_config)