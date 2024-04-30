"""wild_animal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from wild_apk import views

urlpatterns = [
    path('',views.home),
    path('login',views.login_all),
    path('adminhome',views.adminhome),
    path('adminmanage_forestdiv',views.adminmanage_forestdiv),
    path('forestdiv_update/<id>',views.forestdiv_update),
    path('forestdiv_delete/<id>',views.forestdiv_delete),
    path('adminmanage_foreststation',views.adminmanage_foreststation),
    path('update_foreststation/<id>',views.update_foreststation),
    path('delete_foreststation/<id>',views.delete_foreststation),
    path('adminmanage_animal',views.adminmanage_animal),
    path('animal_delete/<id>',views.animal_delete),
    path('admin_view_animals',views.admin_view_animals),
    path('adminmanage_panimals/<id>',views.adminmanage_panimals),
    path('preserved_remove/<id>',views.preserved_remove),
    path('adminmanage_officer',views.adminmanage_officer),
    path('update_officer/<id>',views.update_officer),
    path('delete_officer/<id>',views.delete_officer),
    path('adminallocation',views.adminallocation),
    path('removeallocate/<id>',views.removeallocate),
    path('admin_contactdetails',views.admin_contactdetails),
    path('update_contact/<id>',views.update_contact),
    path('delete_contact/<id>',views.delete_contact),
    path('admincomplaint',views.admincomplaint),
    path('reply/<id>',views.reply),
    path('managecamera/<id>',views.managecamera),
    path('admin_notification',views.admin_notification),
    path('forest_home',views.forest_home),
    path('officer_viewnotification',views.officer_viewnotification),
    path('officer_viewcomplaints',views.officer_viewcomplaints),
    path('officer_forward/<id>',views.officer_forward),
    path('viewcamera',views.viewcamera),
    path('on/<id>',views.on),





    path('apilogin',views.apilogin),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
