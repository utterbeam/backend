from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request,'main/index.html')

def author(request):
	return render(request,'main/author.html')

def post(request):
	return render(request,'main/post.html')