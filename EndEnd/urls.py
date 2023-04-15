
from django.contrib import admin
from django.urls import path
from endapp import views

urlpatterns = [
    path('admin', admin.site.urls,name='ad'),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('loginn', views.loginn, name='loginn'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('hrhome', views.hrhome, name='hrhome'),
    path('driverhome', views.driverhome, name='driverhome'),
    path('hrreg', views.hrreg, name='hrreg'),
    path('driverreg',views.driverreg,name='driverreg'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('addvehicle',views.addvehicle,name='addvehicle'),
    path('addamount',views.addamount,name='addamount'),
    path('servicedetails',views.servicedetails,name='servicedetails'),
    path('insurancedetails',views.insurancedetails,name='insurancedetails'),
    path('viewrequests',views.viewrequests,name='viewrequests'),
    path('viewfeedback',views.viewfeedback,name='viewfeedback'),
    path('workallocation',views.workallocation,name='workallocation'),
    path('reqvehchr', views.reqvehchr, name='reqvehchr'),
    path('requestsend', views.requestsend, name='requestsend'),
    path('viewrequesthr', views.viewrequesthr, name='viewrequestshr'),
    path('requestaccept', views.requestaccept, name='requestaccept'),
    path('hrpayment', views.hrpayment, name='hrpayment'),
    path('reqvehcdriv', views.reqvehcdriv, name='reqvehcdriv'),
    path('requestsenddriv', views.requestsenddriv, name='requestsenddriv'),
    path('viewrequestdriv',views.viewrequestdriv,name='viewrequestdriv'),
    path('requestacceptdriv', views.requestacceptdriv, name='requestacceptdriv'),
    path('viewwork',views.viewwork,name='viewwork'),
    path('workcompleted',views.workcompleted,name='workcompleted'),
    path('viewinsuranceexpiry',views.viewinsuranceexpiry,name='viewinsuranceexpiry'),
    path('feedback', views.feedback, name='feedback'),
    path('dpayment',views.dpayment,name='dpayment'),
    path('choosevehicles',views.choosevehicles,name='choosevehicles'),
    path('viewpayment',views.viewpayment,name='viewpayment'),
    path('card',views.card,name='card'),

    
    
    
    
    
    
    
]

