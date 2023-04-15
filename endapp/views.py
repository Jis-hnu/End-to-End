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
    
            
     
                  

  



