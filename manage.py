#!/usr/bin/env python
from run import app
from flask_script import Manager, Command, Shell

# The Flask-Script extension provides support for writing external scripts in
# Flask, which includes running a development server. For more info, visit:
# http://flask-script.readthedocs.org/en/latest/.
def make_shell_context():
    import os, sys
    return dict(app=app, os=os, sys=sys)

manager = Manager(app)

manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()