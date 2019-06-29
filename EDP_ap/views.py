from django.shortcuts import render
from .models import ProtModel 
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def list_p(request):
    prots = ProtModel.objects.all()

    length = len(prots)

    context = {

        "len"  : length,
        "prots" : prots,
    }
    return render(request, 'index.html', context)


def detail_p(request, prot_id):
    prot = ProtModel.objects.get(id=prot_id)
    context = {

        "protf": prot,
    }
    return render(request, 'prot_detail.html', context)


def send_email_fun(request):
    name = request.POST.get('name', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')

    mssg = """
        """+message+"""

        """+from_email+"""
    """
    print (from_email)
    if subject and message and from_email:
        try:
            send_mail(subject+name, mssg, from_email, ['devsof5e@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
    
