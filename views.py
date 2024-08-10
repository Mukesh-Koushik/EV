from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import mysql.connector
from django.template import loader
from vista.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


con=mysql.connector.connect(database='envirovista',user='root',password='')
cur=con.cursor()


def login_page(request):
    return render(request, 'EnviroVistaloginpage.html')

def login_db(request):
    un=request.GET.get('uname')
    pwd=request.GET.get('pwd')
    s="select * from vista_userinfo where username='"+str(un)+"' and password='"+str(pwd)+"'"
    cur.execute(s)
    d=cur.fetchall()
    if len(d)>0:
        request.session['id']=d[0][0]
        return redirect(home)
    else:
        return redirect(login_page)
    
def logout(request):
    return redirect(login_page)

def register_page(request):
    return render(request, 'EnviroVistaRegisterpage.html')

def register_db(request):
    if request.method == 'POST':
        fn=request.POST.get("t1")
        ln=request.POST.get("t2")
        username=request.POST.get("t3")
        mob_num=request.POST.get("t4")
        password=request.POST.get("t5")
        address=request.POST.get("t6")
        data=UserInfo(fname=fn,lname=ln,username=username,Mob_num=mob_num,password=password,address=address)
        data.save()

    return render(request, 'EnviroVistaloginpage.html')

def home(request):
    return render(request, "HackFestHome.html")

def GCShome(request): 
    cid = request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request,'HackFestGCSpage.html', {'users':users})

def AboutUs(request):
    return render(request, 'EnviroVistaAboutUspage.html')

def Taskshomepage(request  ):
    cid=request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request,'EnviroVistaTaskspage.html',{'users':users}  )

def Tasks_db(request):
    cid=request.session['id']
    user_info = get_object_or_404(UserInfo, pk=cid)
    if request.method == 'POST':
        image1= request.FILES['image1']
        image2= request.FILES['image2']
        image3= request.FILES['image3']
        image4= request.FILES['image4']
        image5= request.FILES['image5']
        image6= request.FILES['image6']
        image7= request.FILES['image7']
        image8= request.FILES['image8']
        video = request.FILES['video']
        tid = request.POST['tid']

        task_info = get_object_or_404(Tasks, pk=tid)
        fs = FileSystemStorage()
        filename = fs.save(video.name, video)
        uploaded_file_url = fs.url(filename)

        task = User_tasks(uid = user_info, task_id = task_info, img1 = image1, img2 = image2, img3 = image3, img4 = image4, img5 = image5, img6 = image6, img7 = image7, img8 = image8, vid1 = 'videos/' + video.name)
        task.save()

        return redirect(Taskcon)
    
    return redirect(Taskshomepage)
    

def Tasks_dbs(request):
    #if request.method == 'POST':
    try:
        # data = json.loads(request.body)
        #     #elements = data.get('elements', [])
        # location = data.get('location', {})
        # latitude = location.get('latitude')
        # longitude = location.get('longitude')
        
        latitude = request.POST.get('latitude', None)
        longitude = request.POST.get('longitude', None)
            
            # Process the elements and location as needed
            #print(f"Received elements: {elements}")
        print(f"User's location: Latitude = {latitude}, Longitude = {longitude}")
        loc = locationsig(lat = latitude, long = longitude)
        loc.save()

            # response = {'status': 'success', 'message': 'Data received successfully', 'received_elements': elements, 'location': location}
            # return JsonResponse(response)

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)


def Taskcon(request):
    return render(request, 'EnviroVistaTasksConPage.html')

def Ecoawarehomepage(request):
    cid=request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request,'EnviroVistaEcoAwarepage.html',{'users':users})

def EcoAware_db(request):
    cid=request.session['id']
    user_info = get_object_or_404(UserInfo, pk=cid)
    if request.method == 'POST':
        image1= request.FILES['image1']
        image2= request.FILES['image2']
        image3= request.FILES['image3']
        image4= request.FILES['image4']
        image5= request.FILES['image5']
        image6= request.FILES['image6']
        image7= request.FILES['image7']
        image8= request.FILES['image8']
        video = request.FILES['video']
        tid = request.POST['tid']

        task_info = get_object_or_404(EcoAware, pk=tid)
        fs = FileSystemStorage()
        filename = fs.save(video.name, video)
        uploaded_file_url = fs.url(filename)

        task = User_Ecoaware(uid = user_info, task_id = task_info, img1 = image1, img2 = image2, img3 = image3, img4 = image4, img5 = image5, img6 = image6, img7 = image7, img8 = image8, vid1 = 'videos/' + video.name)
        task.save()

        return redirect(Ecoawareconpage)
    
    return redirect(Ecoawarehomepage)

def Ecoawareconpage(request):
    return render(request, 'EcoAwareconpage.html')

def Ideaforgehomepage(request  ):
    cid = request.session['id']
    users = Idea_Forge.objects.filter(uid=cid)
    return render(request,'EnviroVistaIdeaForge.html',{'users':users})

def IdeaForge_db(request):
    cid=request.session['id']
    user_info = get_object_or_404(UserInfo, pk=cid)
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        rew = request.POST['reward']
        video_file = request.FILES['video_file']
        fs = FileSystemStorage()
        filename = fs.save(video_file.name, video_file)
        uploaded_file_url = fs.url(filename)

        # Save the video file to the database
        video = Idea_Forge(uid = user_info, task_name = title, task_desc = desc, reward = rew, task_video='videos/' + video_file.name)
        video.save()

        return redirect(Ideaforgeconpage)
    return render(request, 'EnviroVistaIdeaForge.html')

def Ideaforgedispage(request):
    cid=request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request, 'EnviroVistaIdeaForge.html',{'users':users})

def Ideaforgeconpage(request  ):
       
    return render(request,'EnviroVistaIdeaForgecon.html'  )

def Profilepage(request  ):
    cid=request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request,'EnviroVistaProfile.html',{"users":users})

def Addresspage(request  ):
       
    return render(request,'EnviroVistaGCSAddresspage.html'  )

def Editinfo(request):
    cid=request.session['id']
    user_info = get_object_or_404(UserInfo, pk=cid)
    #if request.method == 'POST':
    fname = request.GET.get('fullname')
    lname = request.GET.get('lastname')
    dob = request.GET.get('dob')
    num = request.GET.get('mobile')
    mail = request.GET.get('mail')
    address = request.GET.get('address')
    city = request.GET.get('city')
    state = request.GET.get('state')
    country = request.GET.get('country')
    pincode = request.GET.get('pincode')

    if fname:
        user_info.fname = fname
    if lname:
        user_info.lname = fname
    if mail:
        user_info.username = mail
    if num:
        user_info.Mob_num = num
    if dob:
        user_info.dob = dob
    if address:
        user_info.address = address
    if city:
        user_info.city = city
    if state:
        user_info.state = state
    if country:
        user_info.country = country
    if pincode:
        user_info.pincode = pincode

    
    user_info.save()
    return redirect(Profilepage)    

def Yourorderpage(request  ):
    cid=request.session['id']
    users = Orders.objects.filter(uid=cid)
    return render(request,'EnviroVistayourorderspage.html',{"users":users} )

def Returnrefundpage(request  ):
       
    return render(request,'EnviroVistaRetandRefpage.html'  )

def Gccexchangepage(request  ):
       
    return render(request,'EnviroVistaGCCExchange.html'  )

def Taskpage1(request  ):
       
    return render(request,'EnviroVistaTaskspage1.html'  )

def Taskpage2(request  ):
       
    return render(request,'EnviroVistaTaskspage2.html'  )

def Taskpage3(request  ):
       
    return render(request,'EnviroVistaTaskspage3.html'  )

def Taskpage3_1(request  ):
       
    return render(request,'EnviroVistaTaskspage3(1).html'  )

def Taskpage4(request  ):
       
    return render(request,'EnviroVistaTaskspage4.html'  )

def Taskpage5_1(request  ):
       
    return render(request,'EnviroVistaTaskspage5(1).html'  )

def Taskpage5(request  ):
       
    return render(request,'EnviroVistaTaskspage5.html'  )

def Taskpage6_1(request  ):
       
    return render(request,'EnviroVistaTaskspage6(1).html'  )

def Taskpage6(request  ):
       
    return render(request,'EnviroVistaTaskspage6.html'  )

def Taskpage7(request  ):
       
    return render(request,'EnviroVistaTaskspage7.html'  )

def Taskpage8(request  ):
       
    return render(request,'EnviroVistaTaskspage8.html'  )

def GCScarttojs(request, items=[]):
    cid = request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request, '')

def GCScarttodjango(request):
    if request.method == 'POST':
        request.session['data'] = []
        data = json.loads(request.body)
        # Save the data to the session
        # cart= data.get('key1', [])
        # total = data.get('key2', 0)
        request.session['data'] = data
        # request.session['cart'] = cart
        # request.session['total'] = total
        return JsonResponse({'status': 'success', 'received_data': data})
    return JsonResponse({'status': 'failure'}, status=400)

def GCSpaymentpage(request):
#     # Retrieve the data from the session
    data = request.session.get('data', {})
#     # Retrieve the cart data from cookies
#     #cdata = request.COOKIES.get('cart', '[]')
    
#     #cid = request.session['id']
#     users = Mav.objects.filter(uid=1)

#     # Convert JSON to Python list
#     #data = json.loads(cdata)
#     # total = 0
#     # for item in data:
#     #     temp = item['price']
#     #     total +=int(temp)
#     # print('data',data,'total',total)
#     # a={}
#     #'data':data,
#     # a['total']=total
#     # data.append(a)
#     # #'data': data,
    tota = Mav.objects.filter(id=1)
    return render(request, 'EnviroVistaGCSPaymentpage.html', {'data':data, 'users':tota})
#     return render(request, 'EnviroVistaGCSPaymentpage.html', { 'users':users})

# def GCSpaymentpage(request):
#     total=100
#     cid = request.session['id']
#     users = UserInfo.objects.filter(id=cid)
#     return render(request, 'EnviroVistaGCSPaymentpage.html', {'total':total, 'users':users})
    

def GCSpage(request):
    cid = request.session['id']
    tota = Mav.objects.filter(uid_id=cid)
    data = request.session.get('data', {})
    return render(request, 'EnviroVistaGCSPaymentpage.html', {'data':data, 'users':tota})

def gettotal(request):
    cid = request.session['id']
    user_info = get_object_or_404(UserInfo, pk=cid)
    tota = request.GET.get('tot')

    dev = Mav(uid = user_info, total = tota)
    dev.save()

    #return redirect(GCSpaymentpage)
    return redirect(GCSpage)

def revform(request):
    return render(request, 'Envirovistasubmitreviewform.html')

def gettot(request):
    cid = request.session['id']
    users = Mav.objects.filter(uid=cid)
    return render(request, 'Demo.html', {'users':users})

def GCSorderpage(request):
    data = request.session.get('data', {})
    
    return render(request, 'EnviroVistaGCSPaymentpage.html', {'data':data})

def Gcsprod1(request):
    cid = request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request,'EnviroVistaGCSproductspage1.html',{'users':users})

def Gcsprod2(request  ):
    cid = request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request,'EnviroVistaGCSproductspage2.html' ,{'users':users} )

def Gcsprod3(request):
    cid = request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request,'EnviroVistaGCSproductspage3.html' ,{'users':users} )

def Gcsprod4(request  ):
    cid = request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request,'EnviroVistaGCSproductspage4.html' ,{'users':users} )

def Gcsprod5(request  ):
    cid = request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request,'EnviroVistaGCSproductspage5.html' ,{'users':users} )

def Gcsprod6(request  ):
    cid = request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request,'EnviroVistaGCSproductspage6.html' ,{'users':users} )

def Gcsprod7(request  ):
    cid = request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request,'EnviroVistaGCSproductspage7.html' ,{'users':users} )

def Gcsprod8(request  ):
    cid = request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request,'EnviroVistaGCSproductspage8.html' ,{'users':users} )

def Gcsprod9(request  ):
    cid = request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request,'EnviroVistaGCSproductspage9.html' ,{'users':users} )

def Gcsprod10(request  ):
    cid = request.session['id']
    users = UserInfo.objects.filter(id=cid)
    return render(request,'EnviroVistaGCSproductspage10.html' ,{'users':users}  )

def Ordercon(request):
    return render(request, 'EnviroVistaGCSOrderConpage.html')

def Ecoawarepage1(request  ):
    return render(request,'EnviroVistaEcoAwarepage1.html'  )

def Ecoawarepage2(request  ):
    return render(request,'EnviroVistaEcoAwarepage2.html'  )

def Ecoawarepage3(request  ):
    return render(request,'EnviroVistaEcoAwarepage3.html'  )

def Ecoawarepage4(request  ):
    return render(request,'EnviroVistaEcoAwarepage4.html'  )

def Ecoawarepage5(request  ):
       
    return render(request,'EnviroVistaEcoAwarepage5.html'  )

def Ecoawarepage6(request  ):
       
    return render(request,'EnviroVistaEcoAwarepage6.html'  )

def Ecoawarepage7(request  ):
       
    return render(request,'EnviroVistaEcoAwarepage7.html'  )

def Ecoawarepage8(request  ):
       
    return render(request,'EnviroVistaEcoAwarepage8.html'  )

def Ecoawarepage9(request  ):
       
    return render(request,'EnviroVistaEcoAwarepage9.html'  )

def Ecoawarepage10(request  ):
       
    return render(request,'EnviroVistaEcoAwarepage10.html'  )

def Ecoawarepage11(request  ):
       
    return render(request,'EnviroVistaEcoAwarepage11.html'  )

def Ecoawarepage12(request  ):
       
    return render(request,'EnviroVistaEcoAwarepage12.html'  )

def Ecoawarepage13(request  ):
       
    return render(request,'EnviroVistaEcoAwarepage13.html'  )

def Ecoawarepage14(request  ):
       
    return render(request,'EnviroVistaEcoAwarepage14.html'  )

def Ecoawarepage15(request  ):
       
    return render(request,'EnviroVistaEcoAwarepage15.html'  )


