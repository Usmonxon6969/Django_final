from django.shortcuts import render
from mysite.models import Company, Banner, Service, About, Worker


# Create your views here.
def index(request):
    company = Company.objects.all().order_by('-id')[0:1]
    banner = Banner.objects.all()
    service = Service.objects.all()
    about = About.objects.all().order_by('-id')[0:1]
    worker = Worker.objects.all()


    context = {
        'company': company,
        'banner': banner,
        'service': service,
        'about': about,
        'worker': worker
    }
    return render(request, 'index.html', context)
