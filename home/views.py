from django.shortcuts import render, HttpResponse
from home.models import Detail


# Create your views here.
def index(request):
    return render(request , 'index.html')


def detail(request):
    #return render(request,'index.html')
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        detail = Detail(first_name=first_name, last_name=last_name, email=email, phone=phone, password=password, repassword=repassword)
        detail.save()
        #messages.success(request, 'Your message has been sent!')
    return render(request,'detail.html')
    
    #HttpResponse("This is home page")
