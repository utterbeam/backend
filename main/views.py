from django.shortcuts import render
from django.http import HttpResponse
from main.models import Author_detail , write_up
import base64
import json
import requests
from slugify import slugify
from django.contrib.auth.models import User




# Create your views here.

# def index(request):
#     # data_info = write_up.objects.all()
#  #    context_dict = {}
#  #    array = []
#  #    for i in data_info:
#  #        data = {}
#  #        data['backgroundThumb'] = i.image_url
#  #        data['backgroundLarge'] = i.image_url
#  #        data['url'] = "post/" + str(i.url)
#  #        data['heading'] = i.heading
#  #        data['subText'] = i.sub_text
        # author = ['Alex' , 'Zack']
        # data['author'] = author
#  #        data['id'] = str(i.post_id)
#  #        data['id2'] = "button-behaviour md-whiteframe-10dp post-item post-" + str(i.post_id) + " post type-post status-publish format-standard has-post-thumbnail hentry category-hacking category-internet category-technology"
#  #        data['id3'] = "card-post-" + str(i.post_id)
#  #        data['id4'] = "card-content site-palette-yang-1-color height-40vw width-100 min-height-500px max-height-800px link-white-color card-post site-palette-yang-1-color backdrop-dark-gradient-light ktt-backgroundy card-post-" + str(i.post_id) + "-content"
#  #        data['id5'] = "#card-post-" + str(i.post_id)
#  #        array.append(data)

#  #    context_dict['data'] = array
#     return render(request,'main/newTemplate/after_login.html')



WPM = 200
WORD_LENGTH = 4

import math



def estimate_reading_time(texts):
    # texts = extract_url(url)
    filtered_text = len(texts)
    total_words = math.ceil(filtered_text/WORD_LENGTH)
    return  int(math.ceil(total_words/WPM))


def subtext_generator(texts):
    text_list = texts.split(' ')
    text = ''

    for i in range(20):
        text = text + ' ' +text_list[i]
    # texts = extract_url(url)
    
    return  text



def authorF(request,username):
    user_instance = User.objects.get(username = username)
    i = Author_detail.objects.get_or_create(user = user_instance)[0]
    context_dict = {}
    context_dict['imageUrl'] = i.image_url
    context_dict['description'] = i.description
    context_dict['name'] = i.user.first_name
    author_writeups = write_up.objects.filter(user = user_instance)
    array = []

    for i in author_writeups:
        data = {}
        data['backgroundThumb'] = i.image_url
        data['backgroundLarge'] = i.image_url
        data['url'] = "post/" + str(i.url)
        data['heading'] = i.heading
        data['subText'] = i.sub_text
        data['date'] = i.created_at
        data['writeup'] = i.writeup
              
       
        array.append(data)

    print array
    context_dict['data'] = array




    return render(request,'main/newTemplate/author/iherzog/index.html' , context_dict)

def post(request,uid):
    i = write_up.objects.get_or_create(url = uid)[0]
    context_dict = {}
    context_dict['backgroundThumb'] = i.image_url
    context_dict['heading'] = i.heading
    context_dict['subText'] = i.sub_text
    context_dict['writeup'] = i.writeup
    context_dict['author'] = i.user.first_name
    username = i.user.username
    context_dict['username'] = username
    context_dict['date'] = i.created_at
    time = estimate_reading_time(i.writeup)
    context_dict['time'] = time
    

    user_instance = User.objects.get(username = username)
    author_writeups = write_up.objects.filter(user = user_instance)
    array = []


    for i in author_writeups:
        data = {}
        data['backgroundThumb'] = i.image_url
        data['backgroundLarge'] = i.image_url
        data['url'] = "post/" + str(i.url)
        data['date'] = i.created_at
        data['heading'] = i.heading
        data['subText'] = i.sub_text
        data['writeup'] = i.writeup       
       
        array.append(data)

    print array
    context_dict['data'] = array
    return render(request,'main/newTemplate/story/index.html',context_dict)

# def login(request):
#     return render(request,'main/login.html')

def upload(request):
    user_instance = User.objects.get(username = request.user.username)
    i = Author_detail.objects.get_or_create(user = user_instance)[0]
    context_dict = {}
    context_dict['imageUrl'] = i.image_url
    context_dict['description'] = i.description
    context_dict['name'] = i.user.first_name
    return render(request,'main/upload.html' , context_dict)


from django.contrib.auth.decorators import login_required



def index2(request):
    data_info = write_up.objects.all()
    context_dict = {}
    array = []
    for i in data_info:
        data = {}
        data['backgroundThumb'] = i.image_url
        data['backgroundLarge'] = i.image_url
        data['url'] = "post/" + str(i.url)
        data['heading'] = i.heading
        data['subText'] = i.sub_text
        data['username'] = i.user.username       
        data['author'] = i.user.first_name
        data['date'] = i.created_at
        data['id'] = str(i.post_id)
        data['id2'] = "button-behaviour md-whiteframe-10dp post-item post-" + str(i.post_id) + " post type-post status-publish format-standard has-post-thumbnail hentry category-hacking category-internet category-technology"
        data['id3'] = "card-post-" + str(i.post_id)
        data['id4'] = "card-content site-palette-yang-1-color height-40vw width-100 min-height-500px max-height-800px link-white-color card-post site-palette-yang-1-color backdrop-dark-gradient-light ktt-backgroundy card-post-" + str(i.post_id) + "-content"
        data['id5'] = "#card-post-" + str(i.post_id)
        time = estimate_reading_time(i.writeup)
        data['time'] = time
        array.append(data)

    context_dict['data'] = array
    print request.user
    if str(request.user) != "AnonymousUser": 
        user_instance = User.objects.get(username = request.user.username)
        i = Author_detail.objects.get_or_create(user = user_instance)[0]

        context_dict['imageUrl'] = i.image_url

    # print context_dict
    return render(request,'main/newTemplate/index2.html',context_dict)


def uploadWriteup(request):
    # print request.FILES
    client_id = 'ad3002cdda698d8'
    headers = {"Authorization": "Client-ID %s"%(client_id)}
    # print headers
    #file = cStringIO.StringIO(base64.b64decode(request.FILES['file1']))
    api_key = '37ee388bf32de161bb82e3852124c0af4ae40f19'



    writeup = request.POST['comment']
    # print writeup
    
    heading = request.POST['author']
    # print heading

    


    # url = slugify(urlText)
    user_instance = User.objects.get(username = request.user.username)
    newInstance = write_up.objects.create(user = user_instance)
    newInstance.writeup = writeup
    newInstance.heading = heading

    # newInstance.heading = heading
    urlText = str(heading).strip() + '-' + str(newInstance.user.username)
    url = slugify(urlText)
    newInstance.url = url

    newInstance.sub_text = subtext_generator(writeup)
    
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
    newInstance.image_url = img
    newInstance.save()
    return redirect('home')


def image_to_url_converter(image):

    client_id = 'ad3002cdda698d8'
    headers = {"Authorization": "Client-ID %s"%(client_id)}
    # print headers
    #file = cStringIO.StringIO(base64.b64decode(request.FILES['file1']))
    api_key = '37ee388bf32de161bb82e3852124c0af4ae40f19'

    url = "https://api.imgur.com/3/upload.json"
    # image = request.FILES.get('file', None)
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
    image_url = json.loads(j1.text)["data"]["link"]
    # print img
    return image_url
            
# def facebook_login(request):

#     # https://www.facebook.com/v2.12/dialog/oauth?client_id=190043084948279&redirect_uri=https://utterbeam.herokuapp.com/login&state="{st=state123abc,ds=123456789}"

#     code = request.GET.get('code')
#     # print code

#     url = "https://graph.facebook.com/v2.12/oauth/access_token?client_id=190043084948279&redirect_uri=https://utterbeam.herokuapp.com/login&client_secret=41f955c328dfe25ef060e95db961c176&code=" + code


#     r = requests.get(url = url)

#     access_token_json = r.json()

#     access_token = access_token_json['access_token']

#     url_graph_api = "https://graph.facebook.com/v2.12/me?fields=id,name,email,gender,age_range&access_token=" + access_token

#     r = requests.get(url = url_graph_api)

#     user_data_json = r.json()
#     fb_id = user_data_json['id']
#     name = user_data_json['name']

#     user_instance = Author_detail.objects.get_or_create(fb_id = fb_id)[0]
#     user_instance.name = name
#     user_instance.save()

    







#     # url_picture = "https://graph.facebook.com/v2.12/me/picture?type=large&access_token=" + access_token

#     # r = requests.get(url = url_picture)

#     # x = x.encode('utf8')
    


#     data_info = write_up.objects.all()
#     context_dict = {}
#     array = []
#     for i in data_info:
#         data = {}
#         data['backgroundThumb'] = i.image_url
#         data['backgroundLarge'] = i.image_url
#         data['url'] = "post/" + str(i.url)
#         data['heading'] = i.heading
#         data['subText'] = i.sub_text
#         data['username'] = i.user.username       
        # data['author'] = i.user.first_name
#         data['author'] = author
#         data['id'] = str(i.post_id)
#         data['id2'] = "button-behaviour md-whiteframe-10dp post-item post-" + str(i.post_id) + " post type-post status-publish format-standard has-post-thumbnail hentry category-hacking category-internet category-technology"
#         data['id3'] = "card-post-" + str(i.post_id)
#         data['id4'] = "card-content site-palette-yang-1-color height-40vw width-100 min-height-500px max-height-800px link-white-color card-post site-palette-yang-1-color backdrop-dark-gradient-light ktt-backgroundy card-post-" + str(i.post_id) + "-content"
#         data['id5'] = "#card-post-" + str(i.post_id)
#         array.append(data)

#     context_dict['data'] = array
#     context_dict['fb_id'] = fb_id
#     context_dict['name'] = name

#     print context_dict
#     return render(request,'main/newTemplate/after_login.html' , context_dict)


from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'main/newTemplate/after_login.html')




from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

from main.forms import login_form

def login(request):
    data_info = write_up.objects.all()
    context_dict = {}
    array = []
    for i in data_info:
        data = {}
        data['backgroundThumb'] = i.image_url
        data['backgroundLarge'] = i.image_url
        data['url'] = "post/" + str(i.url)
        data['heading'] = i.heading
        data['subText'] = i.sub_text
        data['username'] = i.user.username       
        data['author'] = i.user.first_name
        data['id'] = str(i.post_id)
        data['id2'] = "button-behaviour md-whiteframe-10dp post-item post-" + str(i.post_id) + " post type-post status-publish format-standard has-post-thumbnail hentry category-hacking category-internet category-technology"
        data['id3'] = "card-post-" + str(i.post_id)
        data['id4'] = "card-content site-palette-yang-1-color height-40vw width-100 min-height-500px max-height-800px link-white-color card-post site-palette-yang-1-color backdrop-dark-gradient-light ktt-backgroundy card-post-" + str(i.post_id) + "-content"
        data['id5'] = "#card-post-" + str(i.post_id)
        time = estimate_reading_time(i.writeup)
        data['time'] = time
        data['date'] = i.created_at
        array.append(data)

    context_dict['data'] = array


    form = login_form()
    context_dict['form'] = form

    error_message = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            error_message = "You are not a registered user please sign up"

            form = login_form()

            context_dict['form'] = form
            context_dict['error_message'] = error_message



    return render(request,'main/login.html' , context_dict)

        




from django.shortcuts import render, redirect

from main.forms import SignUpForm , author_detail_form
from django.shortcuts import  get_object_or_404

def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        details_form = author_detail_form(request.POST , request.FILES)

        
        if form.is_valid():
            user_instance = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # profile = details_form.save(commit = False)

            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)

            # form = SignUpForm(request.POST)
            instance = get_object_or_404(Author_detail, user=user)
            

            if details_form.is_valid():
                print "entered author if"
                # profile = author_detail.save(commit = False)
                instance.description = details_form.cleaned_data.get('description')

                # profile.user = user
                # img_url = image_to_url_converter(request.FILES['file'])
                # instance.image_url = img_url
                # # # profile.description = description
                # print "yoyoyo" + img_url
                instance.save()


                

            else:
                print "somethings wrong with the form"  



            image =request.FILES.get('file')
            # print "the image is " + (image)
            img_url = image_to_url_converter(image)

            instance.image_url = img_url
            # # profile.description = description
            print "yoyoyo" + img_url
            instance.save()     




            # profile.user = user
            # # image = details_form.cleaned_data.get('image')
            # # print image
            # # profile.save()


            # img_url = image_to_url_converter(request.FILES['image'])
            # profile.image_url = img_url
            # print img_url
            # profile.save()
            # registered = True
            # profile = details_form.save(commit = False , instance=instance)
            
            return redirect('home')
    else:
        form = SignUpForm()
        details_form = author_detail_form()
    return render(request, 'main/newTemplate/signup.html', {'form': form ,'details_form': details_form })


    
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)

    data_info = write_up.objects.all()
    context_dict = {}
    array = []
    for i in data_info:
        data = {}
        data['backgroundThumb'] = i.image_url
        data['backgroundLarge'] = i.image_url
        data['url'] = "post/" + str(i.url)
        data['heading'] = i.heading
        data['subText'] = i.sub_text
        data['username'] = i.user.username       
        data['author'] = i.user.first_name
        data['id'] = str(i.post_id)
        data['id2'] = "button-behaviour md-whiteframe-10dp post-item post-" + str(i.post_id) + " post type-post status-publish format-standard has-post-thumbnail hentry category-hacking category-internet category-technology"
        data['id3'] = "card-post-" + str(i.post_id)
        data['id4'] = "card-content site-palette-yang-1-color height-40vw width-100 min-height-500px max-height-800px link-white-color card-post site-palette-yang-1-color backdrop-dark-gradient-light ktt-backgroundy card-post-" + str(i.post_id) + "-content"
        data['id5'] = "#card-post-" + str(i.post_id)
        time = estimate_reading_time(i.writeup)
        data['time'] = time
        data['date'] = i.created_at
        array.append(data)

    context_dict['data'] = array
    # print context_dict
    return render(request,'main/newTemplate/index2.html',context_dict)




