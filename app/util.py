import os

from app.config import postdir


def get_post_path(post_name):
    return os.path.join(postdir, post_name + '.md')
