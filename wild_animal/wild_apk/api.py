from flask import *
from database import *
api=Flask(__name__)


@api.route('/apispinner')
def apispinner():
    data={}
    qry="select * from wild_apk_forest_station"
    res=select(qry)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
        
    data['method']="spinner"
    return str(data)

@api.route('/apiregister')
def apiregister():
    data={}
    fname=request.args['fname']
    lname=request.args['lname']
    place=request.args['place']
    phone=request.args['phone']
    email=request.args['email']
    username=request.args['username']
    password=request.args['password']
    forestid=request.args['forestid']
    

    qry="insert into wild_apk_login values(null,'%s','%s','user')"%(username,password)
    res=insert(qry)
    qry2="insert into wild_apk_user values(null,'%s','%s','%s','%s','%s','%s','%s')"%(fname,lname,place,phone,email,forestid,res)
    res2=insert(qry2)
    if res2:
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="register"
    return str(data)


@api.route('/apilogin')
def apilogin():
    data={}
    uname=request.args['uname']
    password=request.args['password']
    qry="select * from wild_apk_login inner join wild_apk_user using(login_id) inner join wild_apk_forest_station using(forest_station_id) where username='%s' and password='%s'"%(uname,password)
    res=select(qry)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    return str(data)


@api.route('/apicom')
def apicom():
    data={}
    title=request.args['title']
    com=request.args['com']
    userid=request.args['userid']
    
    qry="insert into wild_apk_complaints values(null,'%s','%s','pending',curdate(),'%s')"%(title,com,userid)
    res=insert(qry)
    if res:
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="com"
    return str(data)



@api.route('/apiviewcom')
def apiviewcom():
    data={}
    userid=request.args['userid']
    qry="select * from wild_apk_complaints where user_id='%s'"%(userid)
    res=select(qry)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    return str(data)


@api.route('/apicontactdetails')
def apicontactdetails():
    data={}
    qry="select * from wild_apk_contact_details"
    res=select(qry)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    return str(data)



@api.route('/viewanimals')
def viewanimals():
    data={}
    division_id=request.args['division_id']
    
    qry="select * from wild_apk_animal where forest_division_id='%s'"%(division_id)
    res=select(qry)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="viewanimal"
    return str(data)
    
    
@api.route('/apialert')
def alert():
    data={}
    divisionid=request.args['divisionid']
    from datetime import datetime
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M")
    
    qry="SELECT * FROM wild_apk_alert INNER JOIN wild_apk_camera USING(camera_id) INNER JOIN wild_apk_forest_station USING(forest_station_id) where date LIKE '%s%%' AND time LIKE '%s%%' and forest_division_id='%s'"%(current_date,current_time,divisionid)
    res=select(qry)
    print(res,"//////////////////////////////")
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    return str(data)
        
@api.route('/search_animal')
def search_animal():
    data={}
    search=request.args['search']
    id=request.args['divisionid']
    qry="select * from wild_apk_animal where animal_name='%s' and forest_division_id='%s'"%(search,id)
    res=select(qry)
    print(res,"////pppppppppppppppppp")
    if res:
        data['status']="success"
        data['date']=res
    else:
        data['status']="failed"
    data['method']="view_animal"
    return str(data)
        

@api.route('/apiviewdetectedanimals')
def apiviewdetectedanimals():
    data={}
    id=request.args['divisionid']
    qry="SELECT * FROM wild_apk_alert INNER JOIN wild_apk_camera USING(camera_id) INNER JOIN wild_apk_forest_station USING(forest_station_id)  where forest_station_id='%s' GROUP BY TIME"%(id)
    res=select(qry)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    return str(data)


@api.route("/Search_product")
def Search_product():
    data = {}
    print("**************************")
    id=request.args.get('divisionid')
    sr = request.args.get('search')
    print(id)
    print(sr)
    d="select * from wild_apk_animal where animal_name like '{}%' and forest_division_id='{}'".format(sr,id)
    res = select(d)
    print(res)
    if res:
        data['status'] = 'success'
        data['data']=res
    else:
        data['status'] = 'failed'
        
    data['method']='viewanimal'
    
    return str(data)


api.run(debug=True,host="0.0.0.0",port=5000)