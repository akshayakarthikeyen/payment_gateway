from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from .models import Coffee
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'Contact.html')

def money(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount = int(request.POST.get('amount'))*100
        client = razorpay.Client(auth =("rzp_test_7DyWZH61t2dkVI" , "dHjJAexCRZuq7wdDbOqaPmwJ"))
        payment= client.order.create({'amount':amount , 'currency':'INR','payment_capture':'1'})
        coffee = Coffee(name = name , amount =amount ,email =email , payment_id = payment['id'])
        coffee.save()
        return render(request,'money.html',{'payment':payment})

def donate(request):
    return render(request,'donate.html')


@csrf_exempt
def success(request):
    if request.method=='POST':
       a =  (request.POST)
       payment_id = ""
       for key , val in a.items():
           if key == "razorpay_order_id":
               payment_id = val
               break

       user = Coffee.objects.filter(payment_id = payment_id).first()
       user.paid = True
       user.save()

       msg_plain = render_to_string('email.txt')
       msg_html = render_to_string('email.html')

       send_mail("Your donation has been received", msg_plain, settings.EMAIL_HOST_USER,
                 [user.email], html_message = msg_html)

    return render(request,'success.html')
