from django.shortcuts import render
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


# Create your views here.

@csrf_exempt
def contact(request):

    if request.method == 'POST':
        send_mail(
            subject=request.POST.get('username'),
            message=request.POST.get('description'),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.POST.get('email')],
            fail_silently=False,
        )

    return render(request, 'contact/contact.html')
