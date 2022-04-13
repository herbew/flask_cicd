# -*- coding: utf-8 -*-
from __future__ import absolute_import

from run import app

"""
ATTENTION PLEASE UPDATE IF ANY ERROR --
../flask_cicd/envflask_cicd/lib/python3.8/site-packages/flask_script/__init__.py

    ...
    #from flask._compat import text_type
    
    from ._compat import iteritems, text_type
    ...

"""
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