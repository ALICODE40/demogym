from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request,'index.html')

def membership(request):
   return render(request,'membership.html')

def machines(request):
   return render(request,'machines.html')