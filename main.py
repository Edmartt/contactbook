import unittest
import os
from app import create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.cli.command()
def test():
    '''Run the unit test'''
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
