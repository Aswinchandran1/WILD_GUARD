from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from wild_apk.camera import cam
from .models import *

from datetime import datetime


########################################PUBLIC####################################################################################################

def home(request):
    return render(request,"home.html")

def login_all(request):
    if'sub'in request.POST:
        username=request.POST['uname']
        password=request.POST['pass']
        if login.objects.filter(username=username,password=password).exists():
            qa=login.objects.get(username=username,password=password)
            print(username,password)
            if qa:
                print(qa)
                request.session['log']=qa.pk

                if qa.usertype=='admin':
                    return HttpResponse("<script>alert('WELCOME ADMIN');window.location='/adminhome'</script>")
                
                elif qa.usertype=='officer':
                    q1=forest_officer.objects.get(login_id=request.session['log'])
                    if q1:
                        request.session['officer']=q1.pk
                        return HttpResponse("<script>alert('WELCOME OFFICER');window.location='/forest_home'</script>")
        else:
            return HttpResponse("<script>alert('invalid username or password');window.location='/login'</script>")
        
    return render(request,"login.html")


##########################################ADMIN########################################################################################

def adminhome(request):
    return render(request,"adminhome.html")

def adminmanage_forestdiv(request):
    qa=forest_division.objects.all()

    if 'submit' in request.POST:
        divisionname=request.POST['division']

        q1=forest_division(division_name=divisionname)
        q1.save()
        return HttpResponse("<script>alert('Added Successfully');window.location='/adminmanage_forestdiv'</script>")
    

    return render(request,"adminmanage_forestdiv.html",{'qa':qa})

def forestdiv_update(request,id):
    qa=forest_division.objects.all()
    q1=forest_division.objects.get(forest_division_id=id)

    if 'update' in request.POST:
        divisionname=request.POST['division']
        q1.division_name=divisionname
        q1.save()
        return HttpResponse("<script>alert('Updated Successfully');window.location='/adminmanage_forestdiv'</script>")
    
    return render(request,"adminmanage_forestdiv.html",{'qa':qa,'q1':q1}) 

def forestdiv_delete(request,id):
    q1=forest_division.objects.get(forest_division_id=id)
    q1.delete()
    return HttpResponse("<script>alert('Deleted Successfully');window.location='/adminmanage_forestdiv'</script>")


def adminmanage_foreststation(request):
    q1=forest_division.objects.all()
    qa=forest_station.objects.all()
    qb=camera.objects.all()

    if 'submit' in request.POST:
        divid=request.POST['divid']
        station=request.POST['station']
        place=request.POST['place']
        cnum=request.POST['cnum']

        qa=forest_station(station_name=station,place=place,contact_number=cnum,forest_division_id=divid)
        qa.save()
        return HttpResponse("<script>alert('Added Successfully');window.location='/adminmanage_foreststation'</script>")
    
    return render(request,"adminmanage_foreststation.html",{'q1':q1,'qa':qa,'qb':qb})

def update_foreststation(request,id):
    q1=forest_division.objects.all()
    qa=forest_station.objects.all()
    q2=forest_station.objects.get(forest_station_id=id)

    if 'update' in request.POST:
        station=request.POST['station']
        place=request.POST['place']
        cnum=request.POST['cnum']

        q2.station_name=station
        q2.place=place
        q2.contact_number=cnum

        q2.save()
        return HttpResponse("<script>alert('Updated Successfully');window.location='/adminmanage_foreststation'</script>")
    
    return render(request,"adminmanage_foreststation.html",{'q1':q1,'qa':qa,'q2':q2})

def delete_foreststation(request,id):
    q2=forest_station.objects.get(forest_station_id=id)
    q2.delete()
    return HttpResponse("<script>alert('Deleted Successfully');window.location='/adminmanage_foreststation'</script>")

import datetime
def adminmanage_animal(request):
    qa=forest_division.objects.all()
    qb=animal.objects.all()
    if'submit'in request.POST:
        divid=request.POST['divid']
        animals=request.POST['animal']

        img=request.FILES['image']
        date = datetime.now().strftime("%Y%m%d-%H%M%S")+'.jpg'
        fs=FileSystemStorage()
        fs.save(date,img)
        path=fs.url(date)


        q1=animal(animal_name=animals,animal_image=path,forest_division_id=divid)
        q1.save()
        return HttpResponse("<script>alert('Added Successfully');window.location='/adminmanage_animal'</script>")
    
    return render(request,"adminmanage_animal.html",{'qa':qa,'qb':qb})

def animal_delete(request,id):
    qa=animal.objects.get(animal_id=id)
    qa.delete()
    return HttpResponse("<script>alert('Removed Successfully');window.location='/adminmanage_animal'</script>")

def admin_view_animals(request):
    qa=animal.objects.all()
    qb=preserved_animals.objects.all()
    return render(request,"adminmanage_panimals.html",{'qa':qa,'qb':qb})

def adminmanage_panimals(request,id):

    q2=preserved_animals(animal_id=id)
    q2.save()
    return HttpResponse("<script>alert('Added Successfully');window.location='/admin_view_animals'</script>")
    

def preserved_remove(request,id):
    qb=preserved_animals.objects.get(preserved_animal_id=id)
    qb.delete()
    return HttpResponse("<script>alert('Removed Successfully');window.location='/admin_view_animals'</script>")

def adminmanage_officer(request):
    qa=forest_officer.objects.all()
    if'submit'in request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        designation=request.POST['designation']
        uname=request.POST['uname']
        password=request.POST['pass']

        q2=login(username=uname,password=password,usertype='officer')
        q2.save()
        q1=forest_officer(fname=fname,lname=lname,place=place,phone=phone,email=email,designation=designation,login_id=q2.pk)
        q1.save()
        return HttpResponse("<script>alert('Added Successfully');window.location='/adminmanage_officer'</script>")
    
    return render(request,"adminmanage_officer.html",{'qa':qa})

def update_officer(request,id):
    qa=forest_officer.objects.all()
    q1=forest_officer.objects.get(officer_id=id)
    if'update'in request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        designation=request.POST['designation']

        q1.fname=fname
        q1.lname=lname
        q1.place=place
        q1.phone=phone
        q1.email=email
        q1.designation=designation

        q1.save()

        return HttpResponse("<script>alert('Updated Successfully');window.location='/adminmanage_officer'</script>")
    
    return render(request,"adminmanage_officer.html",{'qa':qa,'q1':q1})

def delete_officer(request,id):
    q1=forest_officer.objects.get(officer_id=id)
    q1.delete()
    return HttpResponse("<script>alert('Updated Successfully');window.location='/adminmanage_officer'</script>")

from datetime import datetime
def admin_notification(request):

    if 'submit'in request.POST:
        title=request.POST['title']
        des=request.POST['des']

        qa=notifications(title=title,description=des,date=datetime.today())
        qa.save()
        return HttpResponse("<script>alert('Send Successfully');window.location='/admin_notification'</script>")
    
    return render(request,"admin_notification.html")
    

def adminallocation(request):
    qa=forest_station.objects.all()
    q1=forest_officer.objects.all()
    qc=allocate.objects.all()
    if'submit'in request.POST:
        station=request.POST['station']
        off=request.POST['off']  

        q2=allocate(forest_station_id=station,officer_id=off)
        q2.save()
        return HttpResponse("<script>alert('Allocated Successfully');window.location='/adminallocation'</script>")
    
    return render(request,"adminallocation.html",{'qa':qa,'q1':q1,'qc':qc})

def removeallocate(id):
    q=allocate.objects.get(allocate_id=id)
    q.delete()
    return HttpResponse("<script>alert('Allocated deleted');window.location='/adminallocation'</script>")



def admin_contactdetails(request):
    qa=contact_details.objects.all()
    if'submit'in request.POST:
        name=request.POST['name']
        num=request.POST['num']
        q1=contact_details(name=name,contact=num)
        q1.save()
        return HttpResponse("<script>alert('Added Successfully');window.location='/admin_contactdetails'</script>")
    
    return render(request,"admin_contactdetails.html",{'qa':qa})

def update_contact(request,id):
    qa=contact_details.objects.all()
    q1=contact_details.objects.get(contact_id=id)

    if'update'in request.POST:
        name=request.POST['name']
        num=request.POST['num']
        q1.name=name
        q1.contact=num
        q1.save()
        return HttpResponse("<script>alert('Updated Successfully');window.location='/admin_contactdetails'</script>")
    return render(request,"admin_contactdetails.html",{'qa':qa,'q1':q1})

def delete_contact(request,id):
    q1=contact_details.objects.get(contact_id=id)
    q1.delete()
    return HttpResponse("<script>alert('Deleted Successfully');window.location='/admin_contactdetails'</script>")

def admincomplaint(request):
    try:
        qa=complaints.objects.filter(reply='checked')
        return render(request,"admincomplaint.html",{'qa':qa})
    except:
        return render(request,"admincomplaint.html")
    
def reply(request,id):
    # q2="1"
    qa=complaints.objects.get(complaints_id=id)
    qa.reply='resolved'
    qa.save()
    return HttpResponse("<script>alert('Complaint Resolved');window.location='/admincomplaint'</script>")
    # return render(request,"admincomplaint.html",{'q2':q2})

def managecamera(request,id):
    if'submit'in request.POST:
        cname=request.POST['cname']
        latitude=request.POST['latitude']
        longitude=request.POST['longitude']
        print(id)
        qa=camera(camera_name=cname,latitude=latitude,longitude=longitude,forest_station_id=id)
        qa.save()
        return HttpResponse("<script>alert('ADDED ');window.location='/adminmanage_foreststation'</script>")
    
    return render(request,"managecamera.html") 



################################################FOREST OFFICER#######################################################################################

def forest_home(request):
    return render(request,"forest_home.html")

def officer_viewnotification(request):
    qa=notifications.objects.all()
    return render(request,"officer_viewnotification.html",{'qa':qa})

def officer_viewcomplaints(request):

    qa=complaints.objects.filter(reply="pending").exists
    if qa:
        q1=complaints.objects.filter(reply="pending")
        return render(request,'officer_viewcomplaints.html',{'q1':q1})
    else:
        return render(request,'officer_viewcomplaints.html')

def officer_forward(request,id):
    qa=complaints.objects.get(complaints_id=id)
    qa.reply="checked"
    qa.save()
    return HttpResponse("<script>alert('FORWARDED');window.location='/officer_viewcomplaints'</script>")




def viewcamera(request):
    try:
        q1=allocate.objects.get(officer_id=request.session['officer'])
        stid=q1.forest_station_id
        qry=camera.objects.filter(forest_station_id=stid)
        return render(request,"officer_viewcamera.html",{'qa':qry})
    except:
        return render(request,"officer_viewcamera.html")


       

def on(request,id):
    cam(id)


# def apilogin(request):
    
def apilogin(request):
    username = request.POST.get('uname')
    print(username)
    password = request.POST.get('password')
    if login.objects.filter(username=username, password=password).exists():
        qa = login.objects.get(username=username, password=password)
        lid = qa.pk
        print(lid)
        if qa.usertype == 'user':
            qs = user.objects.get(LOGIN_id=lid)
            if qs:
                uid = qs.pk
                print(uid)
                return JsonResponse({'status': 'ok','login_id':lid, 'user_id': uid,'forest_station_id':qs.forest_station_id,'forest_division_id':qs.forest_station.forest_division_id})
        else:
            return JsonResponse({'status': 'no'})
    else:
        return JsonResponse({'status': 'no'})




# @api.route('/viewanimals')
def viewanimals(request):
    data={}
    division_id=request.GET['division_id']
    qry=animal.objects.filter(forest_division_id=division_id)
    # qry="select * from wild_apk_animal where forest_division_id='%s'"%(division_id)
    
    if qry:
        data['status']="success"
        data['data']=qry
    else:
        data['status']="failed"
    data['method']="viewanimal"
    return str(data)