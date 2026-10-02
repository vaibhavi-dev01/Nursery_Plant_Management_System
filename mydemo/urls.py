"""
URL configuration for mydemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
#username=plant #password:plantsystem123
from django.contrib import admin
from django.urls import path
from mydemo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.myhome),
    path('login/',views.mylogin),
    path('signup/',views.mysignup),
    path('about/',views.myabout),
    path('us/',views.mycontact),
    path('con/',views.mycontactpage),
    path('adminhome/',views.myadminhome),
    path('userhome/',views.myuserhome),
    path('fedback/',views.myfeedback),
    path('address/',views.myaddress),
    path('userinfo/',views.myuserinfo),
    path('count/',views.mynouser),
    path('plantinfo/',views.myplantinfo),
    path('flowers/',views.myflowers),
    path('fl1/',views.mybyefl1),
    path('fl2/',views.mybyefl2),
    path('fl3/',views.mybyefl3),
    path('fl4/',views.mybyefl4),
    path('fl5/',views.mybyefl5),
    path('fl6/',views.mybyefl6),
    path('fl7/',views.mybyefl7),
    path('fl8/',views.mybyefl8),
    path('fl9/',views.mybyefl9),
    path('fl10/',views.mybyefl10),
    path('fl11/',views.mybyefl11),
    path('fl12/',views.mybyefl12),
    
    path('garden/',views.mygarden),
    path('gar1/',views.mygar1),
    path('gar2/',views.mygar2),
    path('gar3/',views.mygar3),
    path('gar4/',views.mygar4),
    path('gar5/',views.mygar5),
    path('gar6/',views.mygar6),
    path('gar7/',views.mygar7),
    path('gar8/',views.mygar8),
    path('gar9/',views.mygar9),
    path('gar10/',views.mygar10),
    path('gar11/',views.mygar11),
    path('gar12/',views.mygar12),
    
    path('fruits/',views.myfruit),
    path('fru1/',views.myfru1),
    path('fru2/',views.myfru2),
    path('fru3/',views.myfru3),
    path('fru4/',views.myfru4),
    path('fru5/',views.myfru5),
    path('fru6/',views.myfru6),
    path('fru7/',views.myfru7),
    path('fru8/',views.myfru8),
    path('fru9/',views.myfru9),
    path('fru10/',views.myfru10),
    path('fru11/',views.myfru11),
    path('fru12/',views.myfru12),
    
    path('medi/',views.mymedicine),
    path('medi1/',views.mymedi1),
    path('medi2/',views.mymedi2),
    path('medi3/',views.mymedi3),
    path('medi4/',views.mymedi4),
    path('medi5/',views.mymedi5),
    path('medi6/',views.mymedi6),
    path('medi7/',views.mymedi7),
    path('medi8/',views.mymedi8),
    path('medi9/',views.mymedi9),
    path('medi10/',views.mymedi10),
    path('medi11/',views.mymedi11),
    path('medi12/',views.mymedi12),
    
    path('buy/',views.mybuypage),
    path('order/',views.myorder),
    path('video/',views.myvideo),
]
