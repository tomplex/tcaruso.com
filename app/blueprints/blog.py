from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from app.util import get_post_path
from app.models import Post

blog = Blueprint('blog', __name__, template_folder='templates')

@blog.route('/posts')
def posts():
    return render_template('blog_post.html')


@blog.route('/', defaults={'page': 'index'})
@blog.route('/<post>')
def show(post):
    try:
        p = Post(post)
        return render_template('blog_post.html', post=p)
    except TemplateNotFound:
        abort(404)
