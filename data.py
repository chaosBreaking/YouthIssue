# coding: utf-8
import leancloud
from leancloud import Query
from leancloud import LeanCloudError
from leancloud import Object
import hashlib

class myUser(Object):
    pass

def User_store(new):
    user = myUser()
    uid = new['name']
    ukey = new['key1']
    youth_key = new['youth_key']
    md5 = hashlib.md5()
    md5.update(ukey.encode('utf-8'))
    md5_key = md5.hexdigest()
    user = myUser(name = uid,key = md5_key,youth_key = youth_key)
    # user.set('name',uid)
    # user.set('key',ukey)
    try:
        user.save()
    except LeanCloudError as e:
        return e.error, 502