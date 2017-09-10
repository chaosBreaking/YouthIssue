# coding: utf-8

from leancloud import Engine
from leancloud import LeanEngineError

from app import app
from flask import request


engine = Engine(app)

@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'


@engine.before_save('Todo')
def before_todo_save(todo):
    pass