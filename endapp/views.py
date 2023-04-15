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
        request.session['id']=y[0]
                  

  



