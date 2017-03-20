import os
import re

from app.config import postdir

RE_POST_TITLE = re.compile(r'post_title: (.+)')
RE_POST_TAGS = re.compile(r'post_tags: (.+)')
RE_POST_DATE = re.compile(r'post_date: (.+)')


def get_post_content(post_name):
    with open(os.path.join(postdir, post_name + '.md')) as f:
        return f.read()


class Post:
    def __init__(self, post_name):
        self.raw_content = get_post_content(post_name)
        self._metadata = {}
        self.set_metadata()

    @property
    def post_title(self):
        return self._metadata['title']

    @property
    def post_tags(self):
        return self._metadata['tags']

    @property
    def post_date(self):
        return self._metadata['date']

    @property
    def post_content(self):
        return self._metadata['content']

    def set_metadata(self):
        self._metadata['title'] = RE_POST_TITLE.findall(self.raw_content)[0]
        self._metadata['date'] = RE_POST_DATE.findall(self.raw_content)[0]
        self._metadata['tags'] = RE_POST_TAGS.findall(self.raw_content)[0].split(',')
        self._metadata['content'] = self.raw_content.split('+++')[-1]

    def format_tags(self):
        return ','.join(self.post_tags)

    def __getitem__(self, item):
        return self._metadata[item]
