from flask import Flask
from app.blueprints.blog import blog
from flaskext.markdown import Markdown
from flask_bower import Bower


app = Flask(__name__)

Markdown(app)
Bower(app)

app.register_blueprint(blog, url_prefix='/blog')
