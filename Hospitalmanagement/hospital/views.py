from django.shortcuts import render ,redirect
from .forms import psignup,contactus,a_book
from .models import p_signup,contact_us
from django.contrib.auth import logout
# Create your views here.

def index(request):
    user=request.session.get('user')
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            nusr=psignup(request.POST)
            if nusr.is_valid():
                nusr.save()
                print("Signup Successfully...")
            else:
                print(nusr.errors)
        elif request.POST.get('login')=='login':
            usrnm=request.POST['email']
            usrpas=request.POST['pasword']

            usrid=p_signup.objects.get(email=usrnm)# Get id

            usr=p_signup.objects.filter(email=usrnm,pasword=usrpas)
            if usr:
                print("Login Successfully....")
                request.session['user']=usrnm
                request.session['userid']=usrid.id # Get id
                return redirect('home')
            else:
                print("Login Fail....")
    return render(request,'index.html',{'user':user})
    

def book_appointment(request):
    if request.method=='POST':
        apointment=a_book(request.POST)
        if apointment.is_valid():
            apointment.save()
            print("Appoint Booked")
            return redirect('home')
        else:
            print(apointment.errors)
    return render(request,'p_book_appointment.html')

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})
    
def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        contc=contactus(request.POST)
        if contc.is_valid():
            contc.save()
            print("Messsage Send....")
            return redirect('home')
        else:
            print(contc.errors)
    return render(request,'contactus.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def update_profile(request):
    user=request.session.get('user')
    uid=request.session.get('userid')
    id=p_signup.objects.get(id=uid)
    if request.method=='POST':
        updatefrm=psignup(request.POST)
        if updatefrm.is_valid():
            updatefrm=psignup(request.POST,instance=id)
            updatefrm.save()
            print("Profile Data Updated...")
            return redirect('home')
        else:
            print(updatefrm.errors)
    else:
        print("Somthing Wrong Try again....")
    return render(request,'update_profile.html',{'user':user,'userid':p_signup.objects.get(id=uid)})