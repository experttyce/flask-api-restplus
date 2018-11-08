#! /usr/bin/env python

import os

from flask_script import Manager

from flask_api_restplus import create_app, db


app = create_app(os.getenv('FLASK_API_RESTPLUS_CONFIG', 'development'))
manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


if __name__ == '__main__':
    manager.run()
