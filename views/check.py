# coding: utf-8
import leancloud
from leancloud import Query
from leancloud import LeanCloudError
from data import myUser
from youth_keyDB import YouthDB
import hashlib

query = leancloud.Query('myUser')
keyquery = leancloud.Query('YouthDB')

def checkin(name,password):
    result = query.equal_to("name",name)
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    md5_key = md5.hexdigest()
    try:
        result.first().get('name')
        result.first().get('key')
        if md5_key == result.first().get('key'):
            return 'success'
    except LeanCloudError:
        return 'passfail'
            
def checkadmin(name,password):
    if name == 'youthadmin':
        if password == 'cjhhdfwljdxz':
            return 'success'
    else:
        return 'passfail'

def checksign(User):
    name = User['name']
    key1 = User['key1']
    key2 = User['key2']
    youth_key = User['youth_key']
    fail1 = u'用户名已存在'
    fail2 = u'请输入密码'
    fail3 = u'请输入用户名'
    fail4 = u'两次输入密码不一致'
    fail5 = u'请重复输入密码'
    fail6 = u'有思Key无效'
    u = query.equal_to("name",name)
    youth_key = keyquery.equal_to("youth_key",youth_key)
    # print u.first().get('name')
    # if query.equal_to("name",name)!=EOL:
    #     return fail1
    try:
        u.first().get('name')
        if u.first().get('name') == name:
            return fail1
    except LeanCloudError:
        pass
    try:
        youth_key.first().get('youth_key')
        if youth_key.first().get('youth_key') == youth_key:
            pass
    except LeanCloudError:
        return fail6
    if key1 == None:
        return fail2
    elif name == None:
        return fail3
    elif key1 != key2:
        return fail4
    elif key2 == None:
        return fail5
    else:
        return 'success'
    