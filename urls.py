from django.urls import path,include
from . import views

from .views import dashboard
from .views import sign
urlpatterns = [
    
      path('', views.home, name='home'),
      path('sign/', views.sign, name='sign'),
      path('sign/dashboard.html', views.dashboard, name='dashboard'),
      path('back_to_home/', views.back_to_home, name='back_to_home'),
      path('upload_image/', views.upload_image, name='upload_image'),

]