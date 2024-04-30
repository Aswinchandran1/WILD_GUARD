from django.db import models


class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    usertype=models.CharField(max_length=225)

class forest_officer(models.Model):
    officer_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=225)
    lname=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    designation=models.CharField(max_length=225)

class forest_division(models.Model):
    forest_division_id=models.AutoField(primary_key=True)
    division_name=models.CharField(max_length=225)

class forest_station(models.Model):
    forest_station_id=models.AutoField(primary_key=True)
    forest_division=models.ForeignKey(forest_division,on_delete=models.CASCADE)
    station_name=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    contact_number=models.CharField(max_length=225)

class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    forest_station=models.ForeignKey(forest_division,on_delete=models.CASCADE)
    fname=models.CharField(max_length=225)
    lname=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)

class animal(models.Model):
    animal_id=models.AutoField(primary_key=True)
    forest_division=models.ForeignKey(forest_division,on_delete=models.CASCADE)
    animal_name=models.CharField(max_length=225)
    animal_image=models.ImageField(upload_to='static/')

class preserved_animals(models.Model):
    preserved_animal_id=models.AutoField(primary_key=True)
    animal=models.ForeignKey(animal,on_delete=models.CASCADE)

class notifications(models.Model):
    notification_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=225)
    description=models.CharField(max_length=225)
    date=models.CharField(max_length=225)

class contact_details(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=225)
    contact=models.CharField(max_length=225)

class complaints(models.Model):
    complaints_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    title=models.CharField(max_length=225)
    description=models.CharField(max_length=225)
    reply=models.CharField(max_length=225)
    date=models.CharField(max_length=225)

class camera(models.Model):
    camera_id=models.AutoField(primary_key=True)
    forest_station=models.ForeignKey(forest_division,on_delete=models.CASCADE)
    camera_name=models.CharField(max_length=225)
    latitude=models.CharField(max_length=225)
    longitude=models.CharField(max_length=225)

class allocate(models.Model):
    allocate_id=models.AutoField(primary_key=True)
    officer=models.ForeignKey(forest_officer,on_delete=models.CASCADE)
    forest_station=models.ForeignKey(forest_station,on_delete=models.CASCADE)
    status=models.CharField(max_length=225)

class alert(models.Model):
    alert_id=models.AutoField(primary_key=True)
    camera=models.ForeignKey(camera,on_delete=models.CASCADE)
    description=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    image=models.ImageField(upload_to='static/')
    time=models.CharField(max_length=225)


