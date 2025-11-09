from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import UserRegistration
from home.models import AddBirds
from home.models import TakeAppointment
from home.models import GenerateTicket
from home.models import BirdsCategory
from home.models import UserLogin,OtpCode,PriceMaster
import smtplib
import random
import datetime
import qrcode
from django.core.files.storage import FileSystemStorage
from Birdsanctuary.settings import BASE_DIR
import os
from django.db.models import Avg,Max,Min,Sum,Count

# Create your views here.
def index(request):
    return render(request, 'index.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def user_home(request):
    return render(request, 'user_home.html')


def zoo(request):
    return render(request, 'zoo.html')

def info(request):
    return render(request, 'info.html')

def tickets(request):
    return render(request, 'tickets.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def live(request):
    return render(request, 'live.html')

def reg1(request):
    return render(request, 'reg1.html')

#insert view
def reg (request):
    if request.method=="POST" and request.FILES['file']:

        name = request.POST.get('t1')
        gender=request.POST.get('r1')
        city=request.POST.get('t3')
        address=request.POST.get('t4')
        email=request.POST.get('t2')
        mobile_no=request.POST.get('t5')
        visitor_type=request.POST.get('visitor_type')
        password = request.POST.get('t7')
        id_proof=request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(id_proof.name, id_proof)
        upload_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)

        count=UserRegistration.objects.filter(email=email).count()
        if count>=1:
            return render(request,'reg.html',{'This user has already exist'})
        else:
            content = "Thank you for registration"
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('kavyabhegde859@gmail.com', 'ignhyaqclqormgwx')
            mail.sendmail('kavyabhegde859@gmail.com', email, content)
            UserRegistration.objects.create(name=name,gender=gender,city=city,address=address,email=email,mobile_no=mobile_no,visitor_type=visitor_type,id_proof=id_proof)
            UserLogin.objects.create(username=email,password=password,utype='user')
        
        #return redirect('/login')
        return render(request,'reg.html',{'msg':'registered successfully'})
    
    return render(request,'reg.html')

def add_birds(request):
    if request.method=="POST":

        category_name= request.POST.get('t1')
        bird_name=request.POST.get('t2')
        country=request.POST.get('t3')
        image=request.POST.get('t4')
        description=request.POST.get('t5')
        AddBirds.objects.create(category_name=category_name,bird_name=bird_name,country=country,image=image,description=description)
        return redirect('/add_bird_view')
        
        #return render(request,'add_birds.html',{'msg':'inserted successfully'})
         
    
    return render(request,'add_birds.html')
    

def take_app(request):
    username=request.session['username']
    n=datetime.datetime.now()
    today=n.strftime("%Y-%m-%d")
    udata=UserRegistration.objects.get(email=username)
    visitor_type=udata.visitor_type
    cdata=PriceMaster.objects.get(visitor_type=visitor_type)
    adult_cost=cdata.adult_cost
    children_cost=cdata.children_cost

    if request.method=="POST":
       appointment_date=request.POST.get('t3')
       appointment_timings=request.POST.get('t4')
       no_of_adults=request.POST.get('t5')
       no_of_children=request.POST.get('t6')
       if(request.POST.get('t9') is None):
           shooting_cost=0
       else:
           shooting_cost = request.POST.get('t9')

       TakeAppointment.objects.create(visitor_type=visitor_type,user_id=username,appointment_date=appointment_date,appointment_timings=appointment_timings,no_of_adults= no_of_adults,no_of_children=no_of_children,adult_cost=adult_cost,children_cost=children_cost,shooting_cost=shooting_cost,status='pending',payment_status='pending')
        
       return render(request,'take_app.html',{'msg':'Thank you for Booking','today':today})
        #return render(request,'take_app.html',{'msg':'inserted successfully','today':totday})
    
    return render(request,'take_app.html',{'today':today})
    


def generate_tic(request):
    if request.method=="POST":

       appointment_id = request.POST.get('t1')
       ticket_no=request.POST.get('t2')
       user_id =request.POST.get('t3')
       date =request.POST.get('t4')
       time=request.POST.get('t5')
       terms_condition=request.POST.get('t6')
        
       
       GenerateTicket.objects.create(appointment_id=appointment_id,ticket_no=ticket_no,user_id=user_id,date=date,
                                     time=time,
                                 terms_condition=terms_condition)
        
       return redirect('/generate_view')
       #return render(request,'generate_tic.html',{'msg':'inserted successfully'})
    
    return render(request,'generate_tic.html')

def birds_category(request):
    if request.method=="POST":

       category_name=request.POST.get('t1')
       
        
       
       BirdsCategory.objects.create(category_name=category_name)
        
       return redirect('/bird_cat_view')
       #return render(request,'birds_category.html',{'msg':'inserted successfully'})
    
    return render(request,'birds_category.html')

#views table view
def reg_view(request):
      userdict=UserRegistration.objects.all()
      return render(request,'reg_view.html',{'userdict':userdict})

def add_bird_view(request):
      userdict=AddBirds.objects.all()
      return render(request,'add_bird_view.html',{'userdict':userdict})

def take_app_view(request):
      userdict=TakeAppointment.objects.all()
      return render(request,'take_app_view.html',{'userdict':userdict})

def update_status(request,pk):
    TakeAppointment.objects.filter(id=pk).update(status='Accepted')
    return redirect('/take_app_view')

def pay(request,pk):
    username=request.session['username']
    n=datetime.datetime.now()
    cdate=n.strftime("%Y-%m-%d")
    ctime=n.strftime("%X")
    passno = GenerateTicket.objects.all().aggregate(Max('ticket_no'))['ticket_no__max']
    if passno is None:
        passno=101
    else:
        passno=passno+1
    udata=TakeAppointment.objects.get(id=pk)
    no_of_adults=udata.no_of_adults
    no_of_children=udata.no_of_children
    adult_cost=udata.adult_cost
    children_cost=udata.children_cost
    shooting_cost=udata.shooting_cost
    tot1=no_of_adults*adult_cost
    tot2=no_of_children*children_cost
    total=tot1+tot2+shooting_cost
    data="No of adults:"+str(no_of_adults)+"No of Children"+str(no_of_children)
    if request.method=="POST":
        qr = qrcode.QRCode(version=1,box_size=10,border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color='red', back_color='white')
        qcode = str(pk) + ".png"
        img.save("C:/Users/Hp/PycharmProjects/Birds_Sanctuary/Birdsanctuary/media/" + qcode)
        TakeAppointment.objects.filter(id=pk).update(payment_status='Paid')
        GenerateTicket.objects.create(ticket_no=passno,user_id=username,date=cdate,time=ctime,qrcode=qcode,appointment_id=pk,amount=total,payment_date=cdate)
        return render(request,'pay.html',{'amount':total,'msg':'Payment has been done successfully'})

    return render(request,'pay.html',{'amount':total})

def view_ticket(request,pk):
    udata=GenerateTicket.objects.get(appointment_id=pk)
    uid=udata.user_id
    mdata=UserRegistration.objects.get(email=uid)
    name=mdata.name
    address=mdata.address
    vtype=mdata.visitor_type
    qrcode=udata.qrcode
    userdict = GenerateTicket.objects.filter(appointment_id=pk).values()
    return render(request,'view_ticket.html',{'userdict':userdict,'name':name,'address':address,'vtype':vtype,'qrcode':qrcode})


def take_app_search(request):
    userdict = TakeAppointment.objects.all()
    if request.method=="POST":
        search=request.POST.get('search')
        userdict = TakeAppointment.objects.filter(id=search).values()
        return render(request, 'take_app_view_search.html', {'userdict': userdict})
    return render(request, 'take_app_view_search.html', {'userdict': userdict})



def my_ticket(request):
    username = request.session['username']
    userdict = TakeAppointment.objects.filter(user_id=username).values()
    return render(request, 'my_ticket.html', {'userdict': userdict})

def take_app_status(request):
    username=request.session['username']
    userdict = TakeAppointment.objects.filter(user_id=username).values()
    return render(request, 'take_app_status.html', {'userdict': userdict})

def generate_view(request):
      userdict=GenerateTicket.objects.all()
      return render(request,'generate_view.html',{'userdict':userdict})

def bird_cat_view(request):
      userdict=BirdsCategory.objects.all()
      return render(request,'bird_cat_view.html',{'userdict':userdict})

#login authentication    
def login(request):
    if request.method=="POST":
        username=request.POST.get('t1')
        password=request.POST.get('t2')
        request.session['username']=username
        count=UserLogin.objects.filter(username=username).count()

        if count>=1:
            udata=UserLogin.objects.get(username=username)
            upass=udata.password
            utype=udata.utype
            if upass == password:

                if utype=="admin":
                    return redirect('/admin_home')
                
                if utype=="user":
                    return redirect('/user_home')
                
            else:
                return render(request,"login.html",{'msg':'invalid password'})
        
        else:
            return render(request,'login.html',{'msg':'invalid username'})
    return render(request,'login.html')

#delete opeartion
def add_bird_del(request,pk):
    uid=AddBirds.objects.get(id=pk)
    uid.delete()
    return redirect('/add_bird_view')

def bird_cat_del(request,pk):
    uid=BirdsCategory.objects.get(id=pk)
    uid.delete()
    return redirect('bird_cat_view')


def take_app_del(request,pk):
    uid=TakeAppointment.objects.get(id=pk)
    uid.delete()
    return redirect('take_app_view')

def generate_del(request,pk):
    uid=GenerateTicket.objects.get(id=pk)
    uid.delete()
    return redirect('generate_view')

def register_del(request,pk):
    uid=UserRegistration.objects.get(id=pk)
    uid.delete()
    return redirect('reg_view')

#edit opearion
def add_bird_edit(request,pk):
    userdict=AddBirds.objects.filter(id=pk).values()
    if request.method=="POST":

        category_name= request.POST.get('t1')
        bird_name=request.POST.get('t2')
        country=request.POST.get('t3')
        image=request.POST.get('t4')
        description=request.POST.get('t5')
        
       
        AddBirds.objects.filter(id=pk).update(category_name=category_name,bird_name=bird_name,country=country,image=image,
                                 description=description)
        return redirect('/add_bird_view')
    return render(request,'add_bird_edit.html',{'userdict':userdict})

def bird_cat_edit(request,pk):
    userdict=BirdsCategory.objects.filter(id=pk).values()
    if request.method=="POST":
       category_name=request.POST.get('t1')
       BirdsCategory.objects.filter(id=pk).update(category_name=category_name)
       return redirect('/bird_cat_view')
    return render(request,'bird_cat_edit.html',{'userdict':userdict})
 
def generate_tic_edit(request,pk):
     userdict=GenerateTicket.objects.filter(id=pk).values()
     if request.method=="POST":

       appointment_id = request.POST.get('t1')
       ticket_no=request.POST.get('t2')
       user_id =request.POST.get('t3')
       date =request.POST.get('t4')
       time=request.POST.get('t5')
       terms_condition=request.POST.get('t6')
        
       
       GenerateTicket.objects.filter(id=pk).update(appointment_id=appointment_id,ticket_no=ticket_no,user_id=user_id,date=date,
                                     time=time,
                                 terms_condition=terms_condition)
        
       return redirect('/generate_view')

     return render(request,'generate_tic_edit.html',{'userdict':userdict})

def take_app_edit(request,pk):
     userdict=TakeAppointment.objects.filter(id=pk).values()
     if request.method=="POST":

       visitor_type= request.POST.get('t1')
       user_id=request.POST.get('t2')
       appointment_date=request.POST.get('t3')
       appointment_timings=request.POST.get('t4')
       no_of_adults=request.POST.get('t5')
       no_of_children=request.POST.get('t6')
       adult_cost=request.POST.get('t7')
       children_cost=request.POST.get('t8')
       shooting_cost=request.POST.get('t9')
       status=request.POST.get('t10')
        
        
       
       TakeAppointment.objects.filter(id=pk).update(visitor_type=visitor_type,user_id=user_id,appointment_date=appointment_date,
                                appointment_timings= appointment_timings, no_of_adults= no_of_adults,
                                no_of_children=no_of_children,adult_cost=adult_cost,children_cost=children_cost,shooting_cost=shooting_cost,
                                 status=status)
       return redirect('/take_app_view')
     return render(request,'take_app_edit.html',{'userdict':userdict})


def register_edit(request,pk):
     userdict=UserRegistration.objects.filter(id=pk).values()
     if request.method=="POST":

        name = request.POST.get('t1')
        gender=request.POST.get('r1')
        city=request.POST.get('t3')
        address=request.POST.get('t4')
        email=request.POST.get('t2')
        mobile_no=request.POST.get('t5')
        visitor_type=request.POST.get('t6')
       
        UserRegistration.objects.filter(id=pk).update(name=name,gender=gender,city=city,address=address,email=email,
                                       mobile_no=mobile_no,visitor_type=visitor_type)
        
        return redirect('/reg_view')
     return render(request,'register_edit.html',{'userdict':userdict})

#forgotpassword
def forgotpass(request):
    if request.method=="POST":
        username=request.POST.get('t1')
        request.session['username']=username
        ucheck=UserLogin.objects.filter(username=username).count()
        if ucheck>=1:
            otp = random.randint(1111, 9999)
            OtpCode.objects.create(otp=otp, status='active')
            content = "Your OTP IS-" + str(otp)
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('kavyabhegde859@gmail.com','ignhyaqclqormgwx')
            mail.sendmail('kavyabhegde859@gmail.com',username,content)
            return redirect('/otp')
            
        else:
            return render(request,'forgotpass.html',{'msg':'Invalid Username'})
    return render(request,'forgotpass.html')


#otp generation
def otp(request):
    if request.method=="POST":
        otp=request.POST.get('t1')
        ucheck=OtpCode.objects.filter(otp=otp).count()
        if ucheck>=1:
            return redirect('/resetpass')
            
        else:
            return render(request,'otp.html',{'msg':'Invalid OTP'})
    return render(request,'otp.html')

#reset password
def resetpass(request):
    username=request.session['username']
    if request.method=="POST":
        newpass=request.POST.get('t1')
        confirmpass=request.POST.get('t2')
        if newpass==confirmpass:
            UserLogin.objects.filter(username=username).update(password=newpass)
            return redirect('login')
        else:
            return render(request,'resetpass.html',{'msg':'New password and confirm password must be same'})
    return render(request,'resetpass.html')



