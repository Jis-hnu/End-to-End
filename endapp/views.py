from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import MySQLdb
import datetime

from django.core.files.storage import FileSystemStorage
db=MySQLdb.connect('localhost','root','','endend')
c=db.cursor()
def index(request):
    return render(request,"index.html")
def loginn(request):
    return render(request,"login.html")
def login(request):
    msg=""
    if(request.POST):
        uname=request.POST.get("username")
        pwd=request.POST.get("password")
        s="select count(*) from login where username='"+str(uname)+"' and password='"+str(pwd)+"'" 
        c.execute(s)
        y=c.fetchone()
        if(y[0]==0):
            msg="user does not  exist"
        else:
            s="select * from login where username='"+str(uname)+"' and password='"+str(pwd)+"'"
            c.execute(s)
            y=c.fetchone()
            request.session['id']=y[0]
            
            if y[1]=='Admin':
                return HttpResponseRedirect("/adminhome")
            elif y[1]=='HR':
                return HttpResponseRedirect("/hrhome")
            elif y[1]=='DRIVER':
                return HttpResponseRedirect("/driverhome")
            
    return render(request,"login.html",{"msg":msg})
def adminhome(request):
    return render(request,"adminhome.html")
def hrhome(request):
    return render(request,"hrhome.html")
def driverhome(request):
    return render(request,"driverhome.html")
def hrreg(request):
    s=""
    k=""
    
    if(request.POST):
        name=request.POST.get("name")
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        password=request.POST.get("password")
        s="select count(*) from tbl_hrreg where name='"+str(name)+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]==0):
            s="insert into tbl_hrreg(name,address,phone,email,password) values('"+str(name)+"','"+str(address)+"','"+str(phone)+"','"+str(email)+"','"+str(password)+"')"
            c.execute(s)
            k="insert into login(user_type,username,password) values('HR','"+str(email)+"','"+str(password)+"')"
            c.execute(k)
            db.commit()
    loadhr=loadhrreg()
            

    return render(request,"hrreg.html",{"loadhr":loadhrreg})
def loadhrreg():
    j= ""
    c.execute("select * from tbl_category")
    j=c.fetchall() 
    return j

def driverreg(request):
    s=""
    k=""
    if(request.POST):
        name=request.POST.get("name")
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        password=request.POST.get("password")
        s="select count(*)  from tbl_driverreg  where name='"+str(name)+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]==0):
            s="insert into tbl_driverreg(name,address,phone,email,password) values('"+str(name)+"','"+str(address)+"','"+str(phone)+"','"+str(email)+"','"+str(password)+"')"
            c.execute(s)
            k="insert into login(user_type,username,password) values('DRIVER','"+str(email)+"','"+str(password)+"')"
            c.execute(k)
            db.commit()

    return render(request,"driverreg.html")
def addcategory(request):
    s=""
    if(request.POST):
        catname=request.POST.get("catname")
        s="select count(*) count from tbl_category where catname='"+str(catname)+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]==0):
            s="insert into tbl_category(catname)values('"+str(catname)+"')"
            c.execute(s)
            db.commit()
    return render(request,"addcategory.html")

def selectcategory():
    data = ""
    c.execute("select * from tbl_category")
    data=c.fetchall() 
    return data
def addvehicle(request):
    m=""
    if(request.POST):
        vehiclename=request.POST.get("vehiclename")
        catid=request.POST.get("catid")
        regno=request.POST.get("regno")
        m="select count(*) count from tbl_vehicle where regno='"+str(regno)+"'"
        c.execute(m)
        i=c.fetchone()
        if(i[0]==0):
            m="insert into tbl_vehicle(catid,vehiclename,regno) values('"+str(catid)+"','"+str(vehiclename)+"','"+str(regno)+"')"
            c.execute(m)
            db.commit()
    catname=selectcategory()
    return render(request,"addvehicle.html",{"m":m,"catname":catname})
def addamount(request):
    n=""
    if(request.POST):
        amount=request.POST.get("amount")
        vehiclename=request.POST.get("vehiclename")
        n="select count(*) count from tbl_amount where amount='"+str(amount)+"'"
        c.execute(n)
        i=c.fetchone()
        if(i[0]==0):
            n="insert into tbl_amount(vehiclename,amount) values('"+str(vehiclename)+"','"+str(amount)+"')"
            c.execute(n)
            db.commit()
    vehiclename=selectvehicle()       
    return render(request,"addamount.html",{"n":n,"vehiclename":vehiclename})

def selectvehicle():
    c.execute("select * from tbl_vehicle")
    data=c.fetchall() 
    return data
def selectamount():
    c.execute("select * from tbl_vehicle")
    data=c.fetchall() 
    return data
def servicedetails(request):
    n=""
    if(request.POST):
        today=datetime.datetime.now()
        vehiclename=request.POST.get("vehiclename")
        regno=request.POST.get("regno")
        n="select count(*) as count from tbl_service where regno='"+str(regno)+"'"
        c.execute(n)
        i=c.fetchone()
        if(i[0]==0):
            n="insert into tbl_service(regno,servicedate) values('"+str(regno)+"','"+str(today)+"')"
            c.execute(n)
            db.commit()
    vehiclename=selectvehicle()
    regno=selectamount()
    return render(request,"service.html",{"n":n,"vehiclename":vehiclename,"regno":regno})







     
                  

  



