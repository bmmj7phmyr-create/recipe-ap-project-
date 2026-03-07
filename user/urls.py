'''
url mappings for the user api Bu dosya User API için URL eşlemelerini içerir.
'''
from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]