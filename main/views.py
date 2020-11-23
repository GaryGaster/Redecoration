from django.shortcuts import render
from django.core.mail import send_mail


def send_order_enquiry(request):
    if request.method == 'POST':
        if request.POST.get('email', False):
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            number = request.POST['number']
            message = request.POST['message']

            message += '\n\n' + name + '\n' + email + '\n' + number
            subject += ' /**\ ' + name + ' /**\ ' + email + '/**\ ' + number

            send_mail(
                subject,
                message,
                'bartosz.marcickiewicz@gmail.com',
                ['bartosz.marcickiewicz@gmail.com'],
                fail_silently=False
            )

    return render(request, 'main/contact.html')

def home(request):
    send_order_enquiry(request)
    return render(request, 'main/home.html')

def authors(request):
    return render(request, 'main/authors.html')

