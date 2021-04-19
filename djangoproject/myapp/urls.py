from django.conf.urls import include, url
from myapp import views as myapp_views
from myapp.views import StaticView,listView
from django.views.generic import TemplateView

urlpatterns = [
    url('hello/', myapp_views.hello, name = 'hello'),
    url('morning/', myapp_views.morning, name = 'morning'),
    url('time/',myapp_views.time,name='time'),
    url('dbop/',myapp_views.crudops,name='dbop'),
    url(r'article/(\d+)/', myapp_views.viewArticle, name = 'article'),
    url(r'^articles/(\d{2})/(\d{4})', myapp_views.viewArticles , name = 'articles'),
    url(r'^sendemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/',myapp_views.sendEmailWithAttach,name='sendemail'),
    url(r'^static/$', StaticView.as_view()),
    url(r'^dreamreals/', listView.as_view()),
    url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
    url(r'^login/', myapp_views.login , name = 'login'),
    url(r'^view/',myapp_views.View, name = 'view'),
    url(r'^profile/',TemplateView.as_view(template_name = 'profile.html')), 
    url(r'^saved/', myapp_views.SaveProfile, name = 'saved'),
    url(r'^userconnection/',myapp_views.formView, name = 'loginform'),
    url(r'^userlogin/', myapp_views.loginView, name = 'loginview'),

  ]