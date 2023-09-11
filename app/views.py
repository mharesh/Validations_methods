from django.http import HttpResponse
from django.shortcuts import render

from app.forms import Studentform

# Create your views here.
def Student(request):
    SFEO = Studentform()
    d={'SFEO':SFEO}
    if request.method == 'POST':
        SFDO = Studentform(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('invalid Data ')

    return render(request,'student.html',d)