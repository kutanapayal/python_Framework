from django.template import RequestContext
from django.shortcuts import render,redirect,render_to_response
from django.views.generic import TemplateView,ListView
import datetime
from myapp.models import Dreamreal
from myapp.forms import LoginForm
from django.http import HttpResponse
from django.core.mail import EmailMessage
from myapp.forms import ProfileForm
from myapp.models import Profile
from django.views.decorators.cache import cache_page

# Create your views here.
from django.http import HttpResponse

def hello(request):
   today = datetime.datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return redirect("https://www.djangoproject.com")
	
def viewArticle(request, articleId):
   """ A view that display an article based on his ID"""
   text = "Displaying article Number : %s" %articleId
   return redirect(articles, year = "2045", month = "02")
	
@cache_page(60 * 15)

def viewArticles(request, year, month):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)

def sendEmailWithAttach(request, emailto):
   html_content = "Comment tu vas?"
   email = EmailMessage("my subject", html_content, "lasaanishoppings@gmail.com", [emailto])
   email.content_subtype = "html"
   
   fd = open('manage.py', 'r')
   email.attach('manage.py', fd.read(), 'text/plain')
   
   res = email.send()
   return HttpResponse('%s'%res)

class StaticView(TemplateView):
   template_name = "static.html"

class listView(ListView):
    template_name = "dreamreal_list.html"
    model = Dreamreal
    context_object_name = 'dreamreals_objects'
#session example
def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      print("In First IF ------------------------------------->")
      if MyLoginForm.is_valid():
         print("In IF ------------------------------------->")
         username = MyLoginForm.cleaned_data['username']
         request.session['username'] = username
   else:
      MyLoginForm = LoginForm()
		
   return render(request, 'loggedin.html', {"username" : username})

#session example
def View(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'loggedin.html', {"username" : username})
   else:
      return render(request, 'login.html', {})

def SaveProfile(request):
   saved = False
   
   if request.method == "POST":
      #Get the posted form
      MyProfileForm = ProfileForm(request.POST, request.FILES)
      print("In First IF ------------------------------------->")
      if MyProfileForm.is_valid():
         print("In IF ------------------------------------->")  
         profile = Profile()
         profile.name = MyProfileForm.cleaned_data["name"]
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         saved = True
   else:
      MyProfileForm = ProfileForm()
		
   return render(request, 'saved.html', locals())


# def hello(request):
#    text = """<h1>welcome to my app !</h1>"""
#    return HttpResponse(text)

def morning(request):
   text = """<h1>good morning !</h1>"""
   return HttpResponse(text)

# #Example of cookies
def loginView(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      print("In First IF ------------------------------------->")
      if MyLoginForm.is_valid():
        print("In IF ------------------------------------->")
        username = MyLoginForm.cleaned_data['username']
   
   else:
      MyLoginForm = LoginForm()
      

   response = render(request, 'loggedin.html', {"username" : username})
   
   response.set_cookie('last_connection', datetime.datetime.now())
   response.set_cookie('username', datetime.datetime.now())
	
   return response

#Example of cookies
def formView(request):
   if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
      username = request.COOKIES['username']
      
      last_connection = request.COOKIES['last_connection']
      last_connection_time = datetime.datetime.strptime(last_connection[:-7], "%Y-%m-%d %H:%M:%S")
      
      if (datetime.datetime.now() - last_connection_time).seconds < 10:
         return render_to_response(request, 'loggedin.html', {"username" : username},  context_instance = RequestContext(request))
      else:
         return render(request, 'login.html', {})
			
   else:
      return render(request, 'login.html', {})


# def viewArticle(request, articleId):
#    text = "Displaying article Number : %s"%articleId
#    return HttpResponse(text)

# def viewArticles(request, month, year):
#    text = "Displaying articles of : %s/%s"%(year, month)
#    return HttpResponse(text)

# def time(request):
#    today = datetime.datetime.now().date()
   
#    return render(request, "show_time.html", {"today" : today})


def time(request):
   today = datetime.datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "time.html", {"today" : today, "days_of_week" : daysOfWeek})

def crudops(request):
   #Creating an entry
   
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   
   #Read ALL entries
   objects = Dreamreal.objects.all()
   res ='Printing all Dreamreal entries in the DB : <br>'
   
   for elt in objects:
      res += elt.name+"<br>"
   
   #Read a specific entry:
   sorex = Dreamreal.objects.get(name = "sorex")
   res += 'Printing One entry <br>'
   res += sorex.name
   
   #Delete an entry
   res += '<br> Deleting an entry <br>'
   sorex.delete()
   
   #Update
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   res += 'Updating entry<br>'
   
   dreamreal = Dreamreal.objects.get(name = 'sorex')
   dreamreal.name = 'thierry'
   dreamreal.save()
   
   return HttpResponse(res)