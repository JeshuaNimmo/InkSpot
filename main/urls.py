from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_profile/', views.create_profile_view, name='create_profile'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),   
    path('artists/', views.artist_list_view, name='artist_list'),
    path('artist/<int:artist_id>/', views.profile_view, name='artist_profile'),
]