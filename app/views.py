from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':123,'b':125,'c':124}
    return render(request,'conditions.html',d)