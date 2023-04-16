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
def insurancedetails(request):
    n=""
    if(request.POST):
        today=datetime.datetime.now()
       
        regno=request.POST.get("regno")
        n="select count(*) as count from tbl_insurance where regno='"+str(regno)+"'"
        c.execute(n)
        i=c.fetchone()
        if(i[0]==0):
            n="insert into tbl_insurance(regno,exdate) values('"+str(regno)+"','"+str(today)+"')"
            c.execute(n)
            db.commit()
    vehiclename=selectvehicle()
    regno=selectamount()
    return render(request,"insurance.html",{"n":n,"regno":regno})
def viewrequests(request):
    return render(request,"insurance.html")
def selectdriver():
    c.execute("select reg.name,log.id from tbl_driverreg  reg join login  log where log.user_type='DRIVER' and log.username=reg.email")
    data=c.fetchall() 
    return data
def workallocation(request):
    n=""
    name=""
    if(request.POST):
        today=datetime.datetime.now()
        work=request.POST.get("work")
        estimatedkm=request.POST.get("estimatedkm")
        estimateddays=request.POST.get("estimateddays")
        wrkload=request.POST.get("wrkload")
        name=request.POST.get("name")
        n="insert into tbl_work(did,work,wdate,estimatedkm,estimateddays,wrkload,status) values('"+str(name)+"','"+str(work)+"','"+str(today)+"','"+str(estimatedkm)+"','"+str(estimateddays)+"','"+str(wrkload)+"','Alloted')"
        c.execute(n)
        db.commit()
    name=selectdriver()
    return render(request,"allocation.html",{"n":n,"name":name})
def reqvehchr(request):
    c.execute("select tbl_vehicle.vehid,tbl_vehicle.vehiclename,tbl_vehicle.regno,tbl_category.catname from tbl_vehicle,tbl_category where tbl_vehicle.catid=tbl_category.catid")
    j=c.fetchall() 
    print(j)
    return render(request,"requestvehiclehr.html",{"j":j})
def choosevehicles(request):   
    data = ""
    reqdate=request.POST.get("reqdate")
    retdate=request.POST.get("retdate")
    catid=request.POST.get("catid")
    c.execute("select * from tbl_vehicle where catid='"+str(catid)+"' and vehid NOT IN (select vehid from tbl_hr_request where (reqdate BETWEEN '"+str(reqdate)+"' and  '"+str(retdate)+"') or (retdate BETWEEN  '"+str(reqdate)+"' and '"+str(retdate)+"'))")
    j=c.fetchall() 
    print(j)
   
    return render(request,"viewchoosevehicles.html",{"j":j,"catname":selectcategory})
def requestsend(request):
    sid=request.session['id']
    id=request.GET.get("id")
    s="insert into tbl_hr_request(hrid,vehid,status) values('"+str(sid)+"','"+str(id)+"','0')"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/reqvehchr")
def viewrequesthr(request):
    c.execute("select login.username, tbl_vehicle.vehiclename, tbl_vehicle.regno, tbl_category.catname,login.id from login, tbl_vehicle, tbl_category, tbl_hr_request where tbl_hr_request.hrid = login.id and tbl_vehicle.vehid = tbl_hr_request.vehid and  tbl_vehicle.catid = tbl_category.catid and  tbl_hr_request.status='0'")
    
    j=c.fetchall() 
    print(j)
    return render(request,"viewrequestdriv.html",{"j":j})
def requestaccept(request):
    id=request.GET.get("id")
    s="update tbl_hr_request set status='1' where drid='"+str(id)+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/viewrequesthr")
def selectpayment(sid):
   
    c.execute("select login.username, tbl_vehicle.vehiclename, tbl_vehicle.regno,tbl_amount.amount,tbl_category.catname,login.id from login, tbl_vehicle, tbl_category,tbl_amount,tbl_hr_request where tbl_hr_request.hrid = login.id and tbl_vehicle.vehid = tbl_hr_request.vehid and  tbl_vehicle.catid = tbl_category.catid and tbl_hr_request.status='1' and tbl_hr_request.hrid='"+str(sid)+"'")
    data=c.fetchall() 
    return data
def hrpayment(request):
    sid=request.session['id']
    selectpay=""
    
    selectpay=selectpayment(sid)

    return render(request,"hrpayment.html",{"selectpayment":selectpay})
def reqvehcdriv(request):
    c.execute("select tbl_vehicle.vehid,tbl_vehicle.vehiclename,tbl_vehicle.regno,tbl_category.catname from tbl_vehicle,tbl_category where tbl_vehicle.catid=tbl_category.catid")
    j=c.fetchall() 
    print(j)
    return render(request,"requestvehicledriv.html",{"j":j})
def requestsenddriv(request):
    sid=request.session['id']
    id=request.GET.get("id")
    s="insert into tbl_driver_request(drid,vehid,status) values('"+str(sid)+"','"+str(id)+"','0')"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/reqvehcdriv")
def viewrequestdriv(request):
    c.execute("select login.username, tbl_vehicle.vehiclename, tbl_vehicle.regno, tbl_category.catname,login.id from login, tbl_vehicle, tbl_category, tbl_driver_request where tbl_driver_request.drid = login.id and tbl_vehicle.vehid = tbl_driver_request.vehid and  tbl_vehicle.catid = tbl_category.catid and  tbl_driver_request.status='0'")
    j=c.fetchall() 
    print(j)
    return render(request,"viewrequestdriv.html",{"j":j})
def requestacceptdriv(request):
    id=request.GET.get("id")
    s="update tbl_driver_request set status='1' where drid='"+str(id)+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/viewrequestdriv")
def viewwork(request):
    sid=request.session['id']
    c.execute("SELECT * FROM tbl_work  where did='"+str(sid)+"' and status='Alloted'")
    j=c.fetchall() 
    print(j)
    return render(request,"viewwork.html",{"j":j})
def workcompleted(request):
    sid=request.session['id']
    id=request.GET.get("id")
    s="update tbl_work set status='completed' where did='"+str(sid)+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/viewwork")
def viewinsuranceexpiry (request):
    c.execute("SELECT tbl_insurance.`exdate`,tbl_vehicle.`vehiclename`,tbl_vehicle.`regno` FROM tbl_vehicle,tbl_insurance WHERE tbl_vehicle.`vehid`=tbl_insurance.`regno` ")
    j=c.fetchall() 
    print(j)
    return render(request,"viewinsuex.html",{"j":j})
def feedback(request):
    n=""
    if(request.POST):

        feedback=request.POST.get("feedback")
        name=request.POST.get("name")
        n="insert into tbl_feedback(drivername,feedback) values('"+str(name)+"','"+str(feedback)+"')"
        c.execute(n)
        db.commit()
    name=selectdriver()
    return render(request,"feedback.html",{"n":n,"name":name})
def viewfeedback(request):
   
    c.execute("SELECT * FROM tbl_feedback")
    j=c.fetchall() 
    print(j)
    return render(request,"viewfeedback.html",{"j":j})
def selectpaymentdriv(seid):
   
    c.execute("select login.username, tbl_vehicle.vehiclename, tbl_vehicle.regno,tbl_amount.amount,tbl_category.catname,login.id from login, tbl_vehicle, tbl_category,tbl_amount,tbl_driver_request where tbl_driver_request.drid = login.id and tbl_vehicle.vehid = tbl_driver_request.vehid and  tbl_vehicle.catid = tbl_category.catid and tbl_driver_request.status='1' and tbl_driver_request.drid='"+str(seid)+"'")
    data=c.fetchall() 
    return data
def dpayment(request):
    seid=request.session['id']
    selectpay=selectpaymentdriv(seid)
    if(request.POST):


        
        selectpay=""
        tdate=datetime.datetime.now()
        tamnt=request.POST.get("tamnt")
        tday=request.POST.get("dayz")
        ds=int(tamnt)*int(tday)
    
 
        s="select count(*) count from tbl_driver_request where drid='"+str(seid)+"'"

        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):

            c.execute("insert into tbl_payment(driverid,paydate,status,tamnt) values('"+str(seid)+"','"+str(tdate)+"','Payed','"+str(ds)+"')")
            db.commit()
            return HttpResponseRedirect("/card")

    return render(request,"dpayment.html",{"selectpaymentdriv":selectpay})
    
def viewpayment(request):
    c.execute("select  distinct reg.name,pay.paydate from tbl_driverreg  reg join login  log join tbl_payment pay on log.id=pay.driverid where pay.status='Payed' and log.username=reg.email") 
   
    j=c.fetchall() 
    print(j)
    return render(request,"viewpayment.html",{"j":j})
def card(request):
    c.execute("select tamnt from tbl_payment where id in (select max(id) from tbl_payment)")
    j=c.fetchall()
    
    if(request.POST):
        cnum=request.POST.get("cnum")
        exdate=request.POST.get("exdate")
        cvv=request.POST.get("cvv")
        
       
        s="insert into tbl_card(cnum,exdate,cvv) values('"+str(cnum)+"','"+str(exdate)+"','"+str(cvv)+"')"
        c.execute(s)
       
        db.commit()
        
    return render(request,"card/index.html",{"j":j})





     
                  

  



