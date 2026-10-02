from django.shortcuts import render
from stud.models import plant
from stud.models import fedback
from stud.models import address
from stud.models import PlantInfo
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import path
def myhome(request):
    return render(request,'home.html')

def mysignup(request):
    context = {'e': ''}
    dict1={'e1':'' }

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        pass1 = request.POST['pass1']
        cpass = request.POST['cpass']
        
        if pass1 != cpass:
            dict1['e1'] = 'Passwords do not match!'
            return render(request, 'signup.html', dict1)


        if plant.objects.filter(em=email).exists():
            context['e'] = 'You already have an account!'
            return render(request, 'signup.html', context)

        s1 = plant(nm=name, em=email, mo=mobile, ps=pass1, cps=cpass)
        s1.save()
        return HttpResponseRedirect('/login')

    return render(request, 'signup.html',context)

def mylogin(request):
    dict2={'e1':'' }
    message={'e3':''}
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['pass']

        s1 = plant.objects.filter(nm=username)

        if not s1.exists():
            message = {'e3':'User not registered. Please create an account.'}
            return render(request,'login.html',message)
        else:
            user = s1.first()
            if user.ps == password:
                if username == 'Admin':
                    return HttpResponseRedirect('/adminhome')
                else:
                    return HttpResponseRedirect('/userhome')
            else:
                dict2['e1'] = 'Incorrect password. Please try again.'
        return render(request, 'login.html', dict2)
    return render(request, 'login.html')

def myabout(request):
    return render(request,'about.html')

def mycontact(request):
   return render(request,'contactus.html')  
   
def mycontactpage(request):
    dict1={'e1':' '}
    if(request.method=='POST'):
        user=request.POST['nm']
        ema=request.POST['em']
        fed=request.POST['fed']
        s1=fedback(name=user,email=ema,fed=fed)
        s1.save()
        if fedback.objects.filter(email=ema).exists():
            dict1={'e1':"Your feedback Submitted Successfully..."}
    return render(request,'contactpage.html',dict1)

def mybuypage(request):

    if request.method == 'POST':
        ema = request.POST['email']
        add = request.POST['add']
        s1 = address(email=ema, add=add)
        s1.save()
        return HttpResponseRedirect('/order')

    return render(request, 'butynowpage.html')


def myorder(request):
    return render(request,'order.html')

def myuserinfo(request):
    s1=plant.objects.all()
    data={
        'e':s1
    }
    return render(request,'userinfo.html',data)

def mynouser(request):
    count = plant.objects.count()
    data1 = {'i': count}
    return render(request, 'nouser.html', data1)

def myplantinfo(request):
    s1=PlantInfo.objects.all()
    data={
        'e':s1
    }
    return render(request, 'plantuser.html',data)


def myfeedback(request):
    s1=fedback.objects.all()
    data={
        'e':s1
    }
    return render(request,'feedback.html',data)

def myaddress(request):
    s1=address.objects.all()
    data={
        'e':s1
    }
    return render(request,'address.html',data)

def myadminhome(request):
    return render(request, 'admindash.html',)

def myuserhome(request):
    return render(request,'userdash.html')

def myflowers(request):
    return render(request,'flowers.html')
def mybyefl1(request):
    return render(request,'byefl1.html')
def mybyefl2(request):
    return render(request,'byefl2.html')
def mybyefl3(request):
    return render(request,'byefl3.html')
def mybyefl4(request):
    return render(request,'byefl4.html')
def mybyefl5(request):
    return render(request,'byefl5.html')
def mybyefl6(request):
    return render(request,'byefl6.html')
def mybyefl7(request):
    return render(request,'byefl7.html')
def mybyefl8(request):
    return render(request,'byefl8.html')
def mybyefl9(request):
    return render(request,'byefl9.html')
def mybyefl10(request):
    return render(request,'byefl10.html')
def mybyefl11(request):
    return render(request,'byefl11.html')
def mybyefl12(request):
    return render(request,'byefl12.html')

def mygarden(request):
    return render(request,'gardenplanrs.html')
def mygar1(request):
    return render(request,'gar1.html')
def mygar2(request):
    return render(request,'gar2.html')
def mygar3(request):
    return render(request,'gar3.html')
def mygar4(request):
    return render(request,'gar4.html')
def mygar5(request):
    return render(request,'gar5.html')
def mygar6(request):
    return render(request,'gar6.html')
def mygar7(request):
    return render(request,'gar7.html')
def mygar8(request):
    return render(request,'gar8.html')
def mygar9(request):
    return render(request,'gar9.html')
def mygar10(request):
    return render(request,'gar10.html')
def mygar11(request):
    return render(request,'gar11.html')
def mygar12(request):
    return render(request,'gar12.html')

def myfruit(request):
    return render(request,'fruits.html')
def myfru1(request):
    return render(request,'fru1.html')
def myfru2(request):
    return render(request,'fru2.html')
def myfru3(request):
    return render(request,'fru3.html')
def myfru4(request):
    return render(request,'fru4.html')
def myfru5(request):
    return render(request,'fru5.html')
def myfru6(request):
    return render(request,'fru6.html')
def myfru7(request):
    return render(request,'fru7.html')
def myfru8(request):
    return render(request,'fru8.html')
def myfru9(request):
    return render(request,'fru9.html')
def myfru10(request):
    return render(request,'fru10.html')
def myfru11(request):
    return render(request,'fru11.html')
def myfru12(request):
    return render(request,'fru12.html')

def mymedicine(request):
    return render(request,'medicinal.html')
def mymedi1(request):
    return render(request,'medi1.html')
def mymedi2(request):
    return render(request,'medi2.html')
def mymedi3(request):
    return render(request,'medi3.html')
def mymedi4(request):
    return render(request,'medi4.html')
def mymedi5(request):
    return render(request,'medi5.html')
def mymedi6(request):
    return render(request,'medi6.html')
def mymedi7(request):
    return render(request,'medi7.html')
def mymedi8(request):
    return render(request,'medi8.html')
def mymedi9(request):
    return render(request,'medi9.html')
def mymedi10(request):
    return render(request,'medi10.html')
def mymedi11(request):
    return render(request,'medi11.html')
def mymedi12(request):
    return render(request,'medi12.html')

def myvideo(request):
    return render(request,'video.html')










