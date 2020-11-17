from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def send_order_enquiry(request):
    if request.method == 'POST':
        if request.POST.get('email', False):
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']

            message += '\n\n' + name + '\n' + email

            send_mail(
                subject,
                message,
                'maciejmarcickiewicz@gmail.com',
                ['ligewo5150@idcbill.com'],
                fail_silently=False
            )

    return render(request, 'main/index.html')

def home(request):
    send_order_enquiry(request)

    return render(request, 'main/index.html')

    return render(request, 'main/index.html')

def send_order_enquiry(request):
    if request.method == 'POST':
        if request.POST.get('email', False):
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']

            message += '\n\n' + name + '\n' + email

            send_mail(
                subject,
                message,
                'maciejmarcickiewicz@gmail.com',
                ['ligewo5150@idcbill.com'],
                fail_silently=False
            )

    return render(request, 'main/index.html')

