from django.urls import path
from . import views

app_name='myapp'

urlpatterns=[
    path('homepage',views.homepage, name='homepageofbaabtra'),
    path('about',views.about, name='aboutbaabtra'),
    path('contact',views.contact, name='contactbaabtra'),
    path('viewpage',views.viewpage, name='toviewpage')
]