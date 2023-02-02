from django.urls import path
from . import views
app_name='app13'
urlpatterns=[
    path('hello',views.hello,name='hello'),
    path('',views.index13,name='index13'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('uploadimage',views.uploadimage,name='uploadimage'), 
    path('gallery',views.gallery,name='gallery'),  
    path('update/<int:id>',views.update,name='update'),  
    path('logouts',views.logouts,name='logouts'),
    path('displayimg/<int:id>',views.displayimg,name='displayimg'),
]