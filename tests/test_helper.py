import os
import re

from flask_testing import TestCase
from src.app import create_app
from src.extensions import db
from src.utils import get_redis_instance


class BaseTestCase(TestCase):

    def create_app(self):
        env = 'unittest'
        app = create_app(env)

        return app

    def setUp(self):
        self.redis = get_redis_instance()
        db.create_all()

    def tearDown(self):
        self.redis.flushall()
        db.session.remove()
        db.drop_all()
