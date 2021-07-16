from django.shortcuts import render
from .models import Employer

# Create your views here.
def homepage(request):
    print('this is the request ', request)

    # query string din baza de date
    all_employers_qs = Employer.objects.all()

    return render(request, 'homepage.html', {
        'framework_name': 'Django',
        'employers':  all_employers_qs
    })
