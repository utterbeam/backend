from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request,'main/newTemplate/index.html')

def author(request):
	return render(request,'main/newTemplate/author/iherzog/index.html')

def post(request):
	return render(request,'main/newTemplate/how-dreams-of-spacefaring-zombies-led-to-the-launch-of-sputnik/index.html')

def login(request):
	return render(request,'main/login.html')

def upload(request):
	return render(request,'main/upload.html')

def index2(request):
	context_dict = {}
	context_dict['backgroundThumb'] = "http://kohette.com/wpthemes/narratium/wp-content/uploads/2017/10/Victo-Ngai-226x300.jpg"
	context_dict['backgroundLarge'] = "http://kohette.com/wpthemes/narratium/wp-content/uploads/2017/10/Victo-Ngai-772x1024.jpg"
	context_dict['heading'] = "The biggest lie about the future is that it's going to look much different from today."
	context_dict['subText'] = "What the Near Future Is Actually Going to Look Like."
	author = ['Alex' , 'Zack']
	context_dict['author'] = author
	print context_dict
	return render(request,'main/newTemplate/index2.html',context_dict)