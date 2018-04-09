from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request,'main/newTemplate/index.html')

def author(request):
	return render(request,'main/newTemplate/author/iherzog/index.html')

def post(request):
	return render(request,'main/newTemplate/how-dreams-of-spacefaring-zombies-led-to-the-launch-of-sputnik/index.html')