from django.urls import path
from . import views
app_name = 'post_app'

urlpatterns = [
    path('',views.Post,name='post'),
    path('<int:pk>/',views.details, name = 'details'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
]