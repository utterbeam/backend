from django.shortcuts import render
from django.http import HttpResponse
from main.models import details
import base64
import json
import requests
from uuid import uuid4 as uuid

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


def uploadWriteup(request):
    # print request.FILES
    client_id = 'ad3002cdda698d8'
    headers = {"Authorization": "Client-ID %s"%(client_id)}
    # print headers
    #file = cStringIO.StringIO(base64.b64decode(request.FILES['file1']))
    api_key = '37ee388bf32de161bb82e3852124c0af4ae40f19'

    newInstance = details.objects.get_or_create(idd = uuid().hex)[0]

    writeup = request.POST['comment']
    # print writeup
    newInstance.writeup = writeup
    
    heading = request.POST['author']
    # print heading
    newInstance.heading = heading
    
    url = "https://api.imgur.com/3/upload.json"
    image = request.FILES.get('file', None)
    encoded_string = base64.b64encode(image.read())

    j1 = requests.post(
        url, 
        headers = headers,
        data = {
            'key': api_key, 
            'image': encoded_string,
            'type': 'base64',
            'name': '1.jpg',
            'title': 'Picture no. 1'
        }
    )
    # print j1
    img = json.loads(j1.text)["data"]["link"]
    # print img
    newInstance.imageUrl = img
    newInstance.save()
    return HttpResponse("your file was uploaded successfully")
            
















