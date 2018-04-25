from django.shortcuts import render
from django.http import HttpResponse
from main.models import Author_detail , write_up
import base64
import json
import requests
from slugify import slugify



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
#  #        author = ['Alex' , 'Zack']
#  #        data['author'] = author
#  #        data['id'] = str(i.post_id)
#  #        data['id2'] = "button-behaviour md-whiteframe-10dp post-item post-" + str(i.post_id) + " post type-post status-publish format-standard has-post-thumbnail hentry category-hacking category-internet category-technology"
#  #        data['id3'] = "card-post-" + str(i.post_id)
#  #        data['id4'] = "card-content site-palette-yang-1-color height-40vw width-100 min-height-500px max-height-800px link-white-color card-post site-palette-yang-1-color backdrop-dark-gradient-light ktt-backgroundy card-post-" + str(i.post_id) + "-content"
#  #        data['id5'] = "#card-post-" + str(i.post_id)
#  #        array.append(data)

#  #    context_dict['data'] = array
#     return render(request,'main/newTemplate/after_login.html')

def authorF(request,name):
    i = Author_detail.objects.get_or_create(name = name)[0]
    context_dict = {}
    context_dict['imageUrl'] = i.image_url
    context_dict['heading'] = i.description
    context_dict['name'] = name
    return render(request,'main/newTemplate/author/iherzog/index.html' , context_dict)

def post(request,uid):
    i = write_up.objects.get_or_create(url = uid)[0]
    context_dict = {}
    context_dict['backgroundThumb'] = i.image_url
    context_dict['heading'] = i.heading
    context_dict['subText'] = i.sub_text
    context_dict['writeup'] = i.writeup
    return render(request,'main/newTemplate/story/index.html',context_dict)

# def login(request):
#     return render(request,'main/login.html')

def upload(request):
    return render(request,'main/upload.html')


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
        author = ['Alex' , 'Zack']
        data['author'] = author
        data['id'] = str(i.post_id)
        data['id2'] = "button-behaviour md-whiteframe-10dp post-item post-" + str(i.post_id) + " post type-post status-publish format-standard has-post-thumbnail hentry category-hacking category-internet category-technology"
        data['id3'] = "card-post-" + str(i.post_id)
        data['id4'] = "card-content site-palette-yang-1-color height-40vw width-100 min-height-500px max-height-800px link-white-color card-post site-palette-yang-1-color backdrop-dark-gradient-light ktt-backgroundy card-post-" + str(i.post_id) + "-content"
        data['id5'] = "#card-post-" + str(i.post_id)
        array.append(data)

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



    writeup = request.POST['comment']
    # print writeup
    
    heading = request.POST['author']
    # print heading

    


    # url = slugify(urlText)

    newInstance = write_up.objects.get_or_create(heading = heading)[0]
    newInstance.writeup = writeup
    # newInstance.heading = heading
    urlText = str(heading).strip() + '-' + str(newInstance.post_id)
    url = slugify(urlText)
    newInstance.url = url
    
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
    return HttpResponse("your file was uploaded successfully")
            
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
#         author = ['Alex' , 'Zack']
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
        author = ['Alex' , 'Zack']
        data['author'] = author
        data['id'] = str(i.post_id)
        data['id2'] = "button-behaviour md-whiteframe-10dp post-item post-" + str(i.post_id) + " post type-post status-publish format-standard has-post-thumbnail hentry category-hacking category-internet category-technology"
        data['id3'] = "card-post-" + str(i.post_id)
        data['id4'] = "card-content site-palette-yang-1-color height-40vw width-100 min-height-500px max-height-800px link-white-color card-post site-palette-yang-1-color backdrop-dark-gradient-light ktt-backgroundy card-post-" + str(i.post_id) + "-content"
        data['id5'] = "#card-post-" + str(i.post_id)
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

from main.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'main/newTemplate/signup.html', {'form': form})


    
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
        author = ['Alex' , 'Zack']
        data['author'] = author
        data['id'] = str(i.post_id)
        data['id2'] = "button-behaviour md-whiteframe-10dp post-item post-" + str(i.post_id) + " post type-post status-publish format-standard has-post-thumbnail hentry category-hacking category-internet category-technology"
        data['id3'] = "card-post-" + str(i.post_id)
        data['id4'] = "card-content site-palette-yang-1-color height-40vw width-100 min-height-500px max-height-800px link-white-color card-post site-palette-yang-1-color backdrop-dark-gradient-light ktt-backgroundy card-post-" + str(i.post_id) + "-content"
        data['id5'] = "#card-post-" + str(i.post_id)
        array.append(data)

    context_dict['data'] = array
    # print context_dict
    return render(request,'main/newTemplate/index2.html',context_dict)




