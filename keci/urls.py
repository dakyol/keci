from django.urls import path
from . import views

urlpatterns = [
    path('', views.keci_home_view, name='keci_home'),
    path('new/', views.new_project_view, name='new_project'),
    path('search/', views.keci_search_view, name='keci_search'),
    path('search/advanced/', views.keci_advanced_search_view, name='keci_advanced_search'),
    path('project/', views.project_view, name='project'),
    path('help/', views.help_view, name='help'),
]