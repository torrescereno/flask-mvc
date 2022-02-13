import unittest
from app import create_app, db

from config.config import TestingConfig


class BaseConfig(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config=TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        self.app_context.pop()
