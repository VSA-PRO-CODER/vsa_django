from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/',views.login_page, name="Login"),
    path('signup/',views.signupPage, name="signup"),
    path('logout/',views.logoutPage, name="logout"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('reg/',views.user_register, name="Ureg"),
    path('upadteuser/<str:pk>/',views.UpdateUser, name="Update"),
    path('updatesalary/',views.Usalary, name="salary"),
    path('feed/',views.feed, name="feed"),
    path('users/',views.users, name="users"),
    path('profile/<str:pk>/',views.profile, name="profile"),
    path('del/<str:pk>/',views.deluser, name="del"),
    path('dels/<str:pk>/',views.delsalary, name="dels"),
]