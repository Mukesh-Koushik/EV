"""
URL configuration for EnviroVista project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from vista.views import *
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from vista import views
from EnviroVista.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name = "loginpage"),
    #path('/<str:mess>', views.login_page, name = "loginpage"),
    #path('home/', views.home, name = "homepage"),
    path('home/', views.home, name = "homepage"),
    #path('accounts/login/?next=/home/', views.home, name = "homepage"),
    path('accounts/login/?next=/home/', views.home, name='homepage'),
    path('register_page/', views.register_page, name = "registerpage"),
    path('login_db/', views.login_db, name='login_db'),
    path('register_page/register_db', views.register_db, name='register_db'), 
    path('gcshome/', views.GCShome, name = "GCShomepage"),
    path('gcsgetdata/', views.GCScarttodjango, name = "GCSgetdata"),
    #path('gcsorder/', views.GCSorderpage, name = "GCSorderpage"),
    path('gcss/', views.GCSpage, name = "GCSorderpage"),
    path('evform/', views.revform, name = "EVform"),
    path('ordercon/', views.Ordercon, name = "Orderconpage"),
    path('gcshome/prodpage1/', views.Gcsprod1, name = "prodpage1"),
    path('gcshome/prodpage2/', views.Gcsprod2, name = "prodpage2"),
    path('gcshome/prodpage3/', views.Gcsprod3, name = "prodpage3"),
    path('gcshome/prodpage4/', views.Gcsprod4, name = "prodpage4"),
    path('gcshome/prodpage5/', views.Gcsprod5, name = "prodpage5"),
    path('gcshome/prodpage6/', views.Gcsprod6, name = "prodpage6"),
    path('gcshome/prodpage7/', views.Gcsprod7, name = "prodpage7"),
    path('gcshome/prodpage8/', views.Gcsprod8, name = "prodpage8"),
    path('gcshome/prodpage9/', views.Gcsprod9, name = "prodpage9"),
    path('gcshome/prodpage10/', views.Gcsprod10, name = "prodpage10"),
    path('aboutus/', views.AboutUs, name = "aboutus"),
    path('demo/', views.gettot, name = "demo"),
    #path('taskshome/', views.Taskshomepage, name = "Taskshomepage"),
    path('tasks/', views.Taskshomepage, name='Taskshomepage'),
    path('tasks/post', views.Tasks_db, name='Tasks_db'),
    path('task/post', views.Tasks_dbs, name='Tasks_dbs'),
    path('taskhome/taskpage1/', views.Taskpage1, name = "taskpage1"),
    path('taskhome/taskpage2/', views.Taskpage2, name = "taskpage2"),
    path('taskhome/taskpage3_1/', views.Taskpage3_1, name = "taskpage3_1"),
    path('taskhome/taskpage3/', views.Taskpage3, name = "taskpage3"),
    path('taskhome/taskpage4/', views.Taskpage4, name = "taskpage4"),
    path('taskhome/taskpage5_1/', views.Taskpage5_1, name = "taskpage5_1"),
    path('taskhome/taskpage5/', views.Taskpage5, name = "taskpage5"),
    path('taskhome/taskpage6_1/', views.Taskpage6_1, name = "taskpage6_1"),
    path('taskhome/taskpage6/', views.Taskpage6, name = "taskpage6"),
    path('taskhome/taskpage7/', views.Taskpage7, name = "taskpage7"),
    path('taskhome/taskpage8/', views.Taskpage8, name = "taskpage8"),
    path('taskscon/', views.Taskcon, name='Taskcon'),
    path('ecoawarehome/', views.Ecoawarehomepage, name = "Ecoawarehomepage"),
    path('ecoawarehome/post', views.EcoAware_db, name = "EcoAware_db"),
    path('ecoawarecon/', views.Ecoawareconpage, name = "Ecoawareconpage"),
    path('ecoawarehome/task1/', views.Ecoawarepage1, name = "ecoaware1"),
    path('ecoawarehome/task2/', views.Ecoawarepage2, name = "ecoaware2"),
    path('ecoawarehome/task3/', views.Ecoawarepage3, name = "ecoaware3"),
    path('ecoawarehome/task4/', views.Ecoawarepage4, name = "ecoaware4"),
    path('ecoawarehome/task5/', views.Ecoawarepage5, name = "ecoaware5"),
    path('ecoawarehome/task6/', views.Ecoawarepage6, name = "ecoaware6"),
    path('ecoawarehome/task7/', views.Ecoawarepage7, name = "ecoaware7"),
    path('ecoawarehome/task8/', views.Ecoawarepage8, name = "ecoaware8"),
    path('ecoawarehome/task9/', views.Ecoawarepage9, name = "ecoaware9"),
    path('ecoawarehome/task10/', views.Ecoawarepage10, name = "ecoaware10"),
    path('ecoawarehome/task11/', views.Ecoawarepage11, name = "ecoaware11"),
    path('ecoawarehome/task12/', views.Ecoawarepage12, name = "ecoaware12"),
    path('ecoawarehome/task13/', views.Ecoawarepage13, name = "ecoaware13"),
    path('ecoawarehome/task14/', views.Ecoawarepage14, name = "ecoaware14"),
    path('ecoawarehome/task15/', views.Ecoawarepage15, name = "ecoaware15"),
    path('ideaforgehome/', views.Ideaforgehomepage, name = "Ideaforgehomepage"),
    path('ideaforgehome/post', views.IdeaForge_db, name = "Ideaforge_db"),
    path('ideaforgedis/', views.Ideaforgedispage, name = "Ideaforgedis"),
    path('ideaforgecon/', views.Ideaforgeconpage, name = "Ideaforgecon"),
    path('gettotal/', views.gettotal, name = "gettotal"),
    path('profile/address/', views.Profilepage, name = "Profilepage"),
    path('profile/address/Editinfo', views.Editinfo, name = "Editinfo"),
    path('profile/logout', views.logout, name = "logout"),
    path('profile/returnrefund/', views.Returnrefundpage, name = "returnrefund"),
    path('profile/yourorders/', views.Yourorderpage, name = "yourorders"),
    path('profile/gccexchange/', views.Gccexchangepage, name = "gccexchange"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)