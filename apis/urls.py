from django.urls import path
from . import views 

urlpatterns = [
    path('github-jobs', views.githubjobs, name='githubjobs'),
    path('oxford-api', views.oxford, name='oxford'),
]