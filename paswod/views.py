from django.shortcuts import render
from emailauth.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def mail(req):
    if req.method =="POST":
        sub="testing of mail verification"
        tomail=req.POST['mail'] 
        msg=req.POST['msg']
        frommail=EMAIL_HOST_USER
        print(tomail,msg,frommail)
        send_mail(sub,msg,frommail,[tomail])
        return HttpResponse("mail successfully sent")
    return render(req,'paswod/mail.html')