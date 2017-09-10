# coding: utf-8
import leancloud
from leancloud import Query
from leancloud import LeanCloudError
from leancloud import Object
import hashlib
from flask import Blueprint,request,redirect,url_for,render_template

fail1 = u'重复录入！'
query = leancloud.Query('YouthDB')
YouthDB_views = Blueprint('input', __name__)
class YouthDB(Object):
    pass

def youth_key_store(User):
    #将str类型name解码为utf-8后与department压缩为key
    try:
        User['name']=User['name'].decode('utf-8')
    except UnicodeEncodeError:
        pass
    
    u = query.equal_to("name",User['name'])
    try:
        u.first().get('name')
        if u.first().get('name') == User['name']:
            return fail1
    except LeanCloudError:
        pass
    key = User['name']+User['department']
    md5 = hashlib.md5()
    md5.update(key.encode('utf-8'))
    md5_key = md5.hexdigest()
    user = YouthDB(name = User['name'],department = User['department'],post = User['post'],uclass = User['class'],phone = User['phone'],youth_key = md5_key)
    try:
        user.save()
    except LeanCloudError as e:
        return 'fail'
    return 'success'
    
def youth_key_get(key):
    pass

@YouthDB_views.route('ewagreb3ewefwegawevw3rb')
def show():
        return render_template('KeyDB.html')


@YouthDB_views.route('',methods=['POST'])
def input():
    User={'name':request.form['name'],'department': request.values.get('department'),'post': request.values.get('post'),'phone':request.form['phone'],'class':request.values.get('class')}
    result = youth_key_store(User)
    if result == 'success':
        return render_template('KeyDB.html',state = u'录入成功')
    else:
        return render_template('KeyDB.html',state = result)