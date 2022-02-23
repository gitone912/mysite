from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import Userform
from service.models import Serve
from news.models import News
from contactus.models import contactnow
from django.core.mail import send_mail,EmailMultiAlternatives

def aboutus(request):
    return HttpResponse("okkkkkkkkkkkkkkkkkkk")

def c(request,course):
    return HttpResponse(course)

def homepage(request):
    # subject='testing mail'
    # form_email='bodichodi1@gmail.com'
    # msg='nothing'
    # to='bsoni9122505056@gmail.com'
    # msg=EmailMultiAlternatives(subject,msg,form_email,[to])
    # msg.send()
    # send_mail(
    #     'Tessting mail',
    #     'here is the message',
    #     'bodichodi1@gmail.com',
    #     ['bsoni9122505056@gmail.com'],
    #     fail_silently=False,
    # )
    # data={
    #     'title': 'homepage',
    #     'a':'the fuck am doing here',
    #     'list':['demon','witch','bitch'],
    #     'students':[{'name':'bancho',
    #                 'phone':9000},
    #                 {'name':'bsdwala',
    #                  'phone':8800}
    #     ]}
    servicesdata= Serve.objects.all()[1:3]
    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
            servicesdata= Serve.objects.filter(service_title=st)
    newsdata= News.objects.all()[1]
    
    return render(request,"index.html",{'servicesdata':servicesdata,'newsdata':newsdata})
    
def contact(request):
    if request.method=='GET':
        output=request.GET.get('output')
    return render(request,'contactu.html',{'output':output})


def contactme(request):
    return render(request,'contactm.html')

def userform(request):
    final=0
    fn=Userform()
    data={'a':fn}
    try:
        if request.method == 'POST':

            n=request.POST.get('num')
            n2=request.POST.get('num2')
            print(n)
            
            url =f'/contact/?output={n}'
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"form.html",data)

def submitform(request):
    return HttpResponse(request)

def calculator(request):
    c =''
    try:
        if request.method=="POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('selection')
            if opr == "+":
                c=n1+n2
            elif opr == "-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c = n1/n2
    except:
        c="you mf eneter correct value"
    print(c)
    return render(request,'calculator.html',{'c':c})

def oddeven(request):
    b=''
    try:
        if request.method=="POST":
            if request.POST.get('num1')=="":
                return render(request,'oddeven.html',{'error':True})
            n1 = eval(request.POST.get('num1'))
            if (n1%2)==0:
                b="even number"
            else:
                b="odd number"
    except:
        b ="error error error"
    return render(request,'oddeven.html',{'b':b})
    
def marksheet(request):
    a = ''
    b = ''
    c= ''
    try:
        if request.method=="POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            n3 = eval(request.POST.get('num3'))
            n4 = eval(request.POST.get('num4'))
            n5 = eval(request.POST.get('num5'))
            a=n1+n2+n3+n4+n5
            b=(a/500)*100
            c=b/5
    except:
        pass
    return render(request,'marksheet.html',{'a':a,'b':b,'c':c})

def newsdetail(request,id):
    newsdetails=News.objects.get(id=id)
    return render(request,'newsdetail.html',{'news':newsdetails})

    
def saveinquiery(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        des= request.POST.get('des')
        da=contactnow(name=name,email=email,des=des)
        da.save()
    return render(request, 'contactu.html')

