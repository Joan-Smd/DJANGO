from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from works.models import register
from works.models import cusfeed
from works.models import userbook
from works.models import newadmin
from works.models import addplaces
from works.models import payments


from django.db import connection


# Create your views here.
def index(request):
    return render(request,'index.html')

def loginadmin(request):
    return render(request,'loginadmin.html')
def loginadmin1(request):
    if request.method == 'POST':
        try:
            log= newadmin.objects.get(
                uname=request.POST["uname"],
                password=request.POST["password"]
            )
            uname = request.POST["uname"]
            ches = newadmin.objects.filter(uname=uname)
            print("user:",log)
            request.session["uname"]=uname
            return render(request,'adminhome.html', {'data': ches,'uname':uname})
        except newadmin.DoesNotExist as e:
            messages.success(request,"Username / Password Invalid")
            return render(request,'loginadmin.html')
def explore(request):
    if request.session.has_key('semail'):
        semail = request.session["semail"]
        return render(request, 'explore.html', {'semail': semail})
    else:
        messages.error(request, "Session Expired Please Login!")
        return render(request, 'login.html')

def login(request):
    return render(request,'login.html')

def logout(request):
    if request.session.has_key('semail'):
        del request.session["semail"]
        return render(request,'index.html')
    else:
        messages.error(request, "Session Expired Please Login!")
        return render(request, 'login.html')
def login1(request):
    if request.method == 'POST':
        try:
            log= register.objects.get(
                email=request.POST["email"],
                password=request.POST["password"]
            )
            request.session['semail']= log.email
            print("user:",log)
            return render(request,'explore.html',{'semail': log.email})
        except register.DoesNotExist as e:
            messages.success(request,"Email / Password Invalid")
            return render(request,'login.html')

def login2(request):
    return render(request,'login2.html')

def login3(request):
    email = request.POST["email"]
    Password = request.POST["password"]
    if request.method == 'POST':
        request.session["semail"]=email
        return render(request, 'explore.html',{'semail':email})
    else:
        return render(request, 'signup.html')

def signup(request):
    data = addplaces.objects.all()
    return render(request,'signup.html',{'data':data})

def signup1(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        date = request.POST["date"]
        place = request.POST["place"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        store = register(username=username, email=email, mobile=mobile, date=date, place=place, password=password, confirmpass=password2)
        check = register.objects.filter(email=email).exists()
        if check:
            messages.warning(request,'Already a User! Please Login')
            return render(request,'login.html')
        else:
            if password == password2:
                store.save()
                messages.success(request,"Welcome to TAJ")
                return render(request, 'login2.html', {'username': username, 'password': password, 'email': email})
            else:
                messages.warning(request, "Password Mismatch")
                return render(request,'signup.html')
    else:
        messages.warning(request,"Invalid")
        return render(request,'signup.html')




def contact(request):
    return render(request,'contact.html')

def contact1(request):
    if request.session.has_key('semail'):
        semail = request.session["semail"]
        return render(request,'contact1.html',{'semail':semail})
    else:
        messages.error(request,"Session Expired Please Login!")
        return render(request,'login.html')
def feedback(request):
    if request.method == 'POST':
        cname= request.POST["name"]
        cemail= request.POST["email"]
        date = request.POST["date"]
        place = request.POST["place"]
        cmessage= request.POST["message"]
        feed = cusfeed(name= cname, email = cemail, date=date, place=place, message = cmessage)
        feed.save()
        messages.success(request,"Thank You")
        return render(request,'feedback.html')

def rooms(request):
    if request.session.has_key('semail'):
        semail = request.session["semail"]
        return render(request,'rooms.html',{'semail':semail})
    else:
        messages.error(request,"Session Expired Please Login!")
        return render(request,'login.html')
def book(request):
    if request.session.has_key('semail'):
        semail = request.session["semail"]
        data = addplaces.objects.all()
        return render(request,'book.html',{'data':data,'semail':semail})
    else:
        messages.error(request,"Session Expired Please Login!")
        return render(request,'login.html')

def book1(request):
    email = request.POST["email"]
    place = request.POST["place"]
    room = request.POST["room"]
    guest = request.POST["guest"]
    date = request.POST["date"]
    checkin = request.POST["checkin"]
    checkout = request.POST["checkout"]
    note = request.POST["note"]
    payment = request.POST["payment"]
    status = request.POST["status"]
    if request.method == 'POST':
        bookings = userbook(email=email,place=place,room=room,guest=guest, date=date, checkin=checkin,checkout=checkout,note=note,payment=payment,status=status)
        bookings.save()
        messages.success(request,"Booking Successful")
        datas = userbook.objects.filter(email=email)
        return redirect("booking")
    else:
        return render(request,'book.html')

def booking(request):
    if request.session.has_key('semail'):
        semail = request.session["semail"]
        datas = userbook.objects.filter(email=semail).order_by('checkin')
        return render(request,'mybooking.html',{'data':datas,'semail':semail})
    else:
        messages.error(request,"Session Expired Please Login!")
        return render(request,'login.html')







def adminregister(request):
    uname = request.session["uname"]
    return render(request,'adminregister.html',{'uname':uname})

def adminregister1(request):
    if request.method == 'POST':
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        uname = request.POST["uname"]
        role = request.POST["role"]
        password = request.POST["password"]
        check = newadmin.objects.filter(uname=uname).exists()
        if check:
            messages.warning(request, 'Already a User! Please Login')
            return render(request, 'loginadmin.html')
        else:
            adminreg = newadmin(fname=fname,lname=lname,uname=uname,role=role,password=password)
            adminreg.save()
            messages.success(request,"New Admin Added Successfully")
            return redirect("viewadmin")
    else:
        return render(request,'adminregister.html')

def viewadmin(request):
    if request.session.has_key('uname'):
        datas = newadmin.objects.all()
        uname = request.session["uname"]
        return render(request,'viewadmin.html',{'data':datas,'uname':uname})
    else:
        messages.error(request, "Session Expired Please Login Again")
        return render(request, 'loginadmin.html')

def deladmin(request,id):
    if request.session.has_key('uname'):
        datas = newadmin.objects.get(id=id)
        datas.delete()
        messages.success(request,"Admin Removed")
        return redirect("viewadmin")
    else:
        messages.error(request, "Session Expired Please Login!")
        return render(request, 'loginadmin.html')

def adminhome(request):
    if request.session.has_key('uname'):
        uname = request.session["uname"]
        return render(request,'adminhome.html',{'uname':uname})
    else:
        messages.error(request,"Session Expired Please Login Again")
        return render(request,'loginadmin.html')
def customers(request):
    if request.session.has_key('uname'):
        allcust = register.objects.all()
        uname =request.session["uname"]
        return render(request,'customers.html',{'allcust':allcust,'uname':uname})
    else:
        messages.error(request,"Session Expired Please Login Again")
        return render(request,'loginadmin.html')

def bookings(request):
    if request.session.has_key('uname'):
        datas = userbook.objects.all().order_by('checkin')
        uname = request.session["uname"]
        return render(request,'bookings.html', {'data': datas,'uname':uname})
    else:
        messages.error(request, "Session Expired Please Login Again")
        return render(request, 'loginadmin.html')
def places(request):
    if request.session.has_key('uname'):
        data = addplaces.objects.all().order_by('id')
        uname = request.session["uname"]
        return render(request,'places.html',{'data':data,'uname':uname})
    else:
        messages.error(request, "Session Expired Please Login Again")
        return render(request, 'loginadmin.html')
def place1(request):
    if request.method == 'POST':
        newplace = request.POST["newplace"]
        check = addplaces.objects.filter(place=newplace).exists()
        if check:
            messages.warning(request, 'Already Place Exists Please Enter New Place')
            return redirect("places")
        else:
            adding = addplaces(place=newplace)
            adding.save()
            messages.success(request,"Place Added Successfully")
            return redirect("places")

def delplace(request,id):
    if request.session.has_key('uname'):
        datas = addplaces.objects.get(id=id)
        datas.delete()
        return redirect("places")
    else:
        messages.error(request, "Session Expired Please Login!")
        return render(request, 'loginadmin.html')

def status(request,id):
    if request.session.has_key('uname'):
        datas = userbook.objects.get(id=id)
        status = "Booked"
        payment= "Success"
        datas.status=status
        datas.payment=payment
        datas.save()
        messages.success(request,"Booking Confirmed")
        return redirect("bookings")
    else:
        messages.error(request, "Session Expired Please Login!")
        return render(request, 'loginadmin.html')

def cancel(request,id):
    if request.session.has_key('semail'):
        datas = userbook.objects.get(id=id)
        status = "Cancel"
        payment= "Cancel"
        datas.status=status
        datas.payment=payment
        datas.save()
        messages.warning(request,"Booking Cancelled")
        return redirect("booking")
    else:
        messages.error(request, "Session Expired Please Login!")
        return render(request, 'login.html')

def delete(request,id):
    if request.session.has_key('uname'):
        datas = userbook.objects.get(id=id)
        datas.delete()
        messages.success(request,"Booking Deleted")
        return redirect("bookings")
    else:
        messages.error(request, "Session Expired Please Login!")
        return render(request, 'loginadmin.html')

def payment(request,id):
    if request.session.has_key('semail'):
        datas = userbook.objects.get(id=id)
        datas.payment= "Success"
        datas.save()
        return render(request,'payment.html',{'data':datas})
    else:
        messages.error(request, "Session Expired Please Login!")
        return render(request, 'login.html')

def payment1(request):
    if request.method == 'POST':
        cname = request.POST["cardname"]
        cnumber = request.POST["cardnumber"]
        expmonth = request.POST["expmonth"]
        expyear = request.POST["expyear"]
        cvv = request.POST["cvv"]
        payment =request.POST["payment"]
        store = payments(cname=cname,cnumber=cnumber,expmonth=expmonth,expyear=expyear,cvv=cvv)
        store.save()
        messages.success(request,"Payment Successfull")
        return redirect("booking")


def adminout(request):
    if request.session.has_key('uname'):
        del request.session["uname"]
        return render(request,'loginadmin.html')
    else:
        messages.error(request, "Session Expired Please Login!")
        return render(request, 'loginadmin.html')