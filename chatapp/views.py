from django.shortcuts import render,redirect
from django.core.mail import send_mail
from . models import registration,Room,chatdata
import random
from wechat import settings
from django.http import HttpResponse,JsonResponse
# Create your views here.
def getmessages(request,room):
    rname=room
    room_details=Room.objects.get(name=rname)
    messages=chatdata.objects.filter(room=room_details.id)
    print("inside get messages")
    print(messages.values())
    return JsonResponse({"messages":list(messages.values())})
def send(request,room):
    chatmessage=request.POST.get("message")
    room_id=request.POST.get("room_id")
    username=request.POST.get("username")
    print(chatmessage,room_id,username)
    new_message=chatdata.objects.create(message=chatmessage,user=username,room=room_id)
    new_message.save()
    return HttpResponse('message sent')
def signin(request):
    global userdata
    if(request.method=="POST"):
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)
        try:
            userdata=registration.objects.get(email=username)
            if(password==userdata.password):
                return redirect("chat/")
            else:
                return render(request,"chatapp/login.html",{"alert":"Password Not Valid"})
        except:
            return render(request,"chatapp/login.html",{"alert":"User Not Valid"})
            
    return render(request,"chatapp/login.html")
def chat(request):
    global chatname
    global rname
    chatrooms=Room.objects.all()
    if request.method=="POST" and "createroom" in request.POST:
        roomname=request.POST.get("chatroom")
        chatname=request.POST.get("user")
        roompassword=request.POST.get("roompassword")
        if(Room.objects.filter(name=roomname).exists()):
            return render(request,"chatapp/chatroom.html",{"msg":"Room Alredy Exists","rooms":chatrooms})
        else:
            new_room=Room.objects.create(name=roomname,password=roompassword)
            new_room.save()
            url="chatapp/{}".format(roomname)
            return redirect(url)
            #return render(request,"chatapp/we.html")
    if request.method=="POST" and "rname" in request.POST:
        rname=request.POST.get("rname")
        rpswd=request.POST.get("entrypswd")
        detcheck=Room.objects.get(name=rname)
        if(detcheck.password==rpswd):
            url="chatapp/{}".format(rname)
            return redirect(url)
        else:
            msg="password not valid"
            return render(request,"chatapp/chatroom.html",{"rooms":chatrooms,"msg":msg})
        #room_details=Room.objects.get(name=rname)
        #return render(request,"chatapp/wechat.html",{"rooms":chatrooms,"room":rname,"room_details":room_details,"chatname":"sabarosh"})
    return render(request,"chatapp/chatroom.html",{"rooms":chatrooms})
def register(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        mobile=request.POST.get("mobile")
        try:
            registration.objects.create(name=name,email=email,password=password,mobile=mobile)
            otp=random.randint(1000,9999)
            message="Hellow, {}\n Thank You for using WeChat,Your Verification number is{}".format(name,str(otp))
            send_mail("WeChat Verification",message,settings.EMAIL_HOST_USER,[email,])
        except:
            return render(request,"chatapp/register.html",{"alert":"User Alredy Exists"})
            
    return render(request,"chatapp/register.html")
def chatpage(request,room):
    roomdetails=Room.objects.get(name=room)
    return render(request,"chatapp/alpha.html",{"room":room,"room_details":roomdetails,"chatname":"sabarish"})
