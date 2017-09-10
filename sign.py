from views.check import checksign
from data import User_store
from flask import render_template,redirect,url_for
def signHandle(User):
    result = checksign(User)
    if result=='success':
        User_store(User)
    return result
