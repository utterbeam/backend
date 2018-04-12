from django.shortcuts import render
from django.http import HttpResponse
from main.models import details

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
    dataInfo = details.objects.all()
    context_dict = {}
    array = []
    for i in dataInfo:
        data = {}
        data['backgroundThumb'] = i.imageUrl
        data['backgroundLarge'] = i.imageUrl
        data['heading'] = i.heading
        data['subText'] = i.subText
        author = ['Alex' , 'Zack']
        data['author'] = author
        array.append(data)
        data['id'] = str(i.idd)
        data['id2'] = "button-behaviour md-whiteframe-10dp post-item post-" + str(i.idd) + " post type-post status-publish format-standard has-post-thumbnail hentry category-hacking category-internet category-technology"
        data['id3'] = "card-post-" + str(i.idd)
        data['id4'] = "card-content site-palette-yang-1-color height-40vw width-100 min-height-500px max-height-800px link-white-color card-post site-palette-yang-1-color backdrop-dark-gradient-light ktt-backgroundy card-post-" + str(i.idd) + "-content"
        data['id5'] = "#card-post-" + str(i.idd)

    objectCount = details.objects.all().count()
    context_dict['data'] = array
    # print context_dict
    return render(request,'main/newTemplate/index2.html',context_dict)




def enterData(request):
    idd = '11'
    newInstance = details.objects.get_or_create(idd = idd)[0]
    newInstance.heading = 'Bad Day'
    newInstance.imageUrl = "http://images.mentalfloss.com/sites/default/files/styles/mf_image_16x9/public/522639-istock-154932729.jpg?itok=W38uZs2Y&resize=1100x619"
    newInstance.subText = "In the 14 years he spent planning the monument, artist Gutzon Borglum harbored a deep concern"
    newInstance.save()


















