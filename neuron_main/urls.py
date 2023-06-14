"""neuron URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from neuron_main import views

urlpatterns = [
    path('', views.home, name="Home Page | Neuron"),
    path('doctors', views.doctors, name="Doctors | Neuron"),
    path('doctors/<str:city>', views.doctors_by_city, name="doctors_by_city"),
    path('therapy', views.therapy, name="Therapy | Neuron"),
    path('therapy/<int:sid>', views.peronalized_therapy, name="therapy_personalized"),
    path('game', views.game, name="Games | Neuron"),
    path('game/<int:sid>', views.peronalized_games, name="games_personalized"),

    path('quiz', views.quiz, name="Quiz | Neuron"),
    path('blogs', views.blogs, name="Blogs | Neuron"),
    path('stories', views.stories, name="stories | Neuron"),
    path('stories/<int:sid>', views.personalized_stories, name="personalized_stories"),
    path('analytics', views.analytics, name="analytics"),
    
    # Auth related Views

    path('login', views.login, name="Login | Neuron"),
    path('signup', views.signup, name="SignUp | Neuron"),
    path('logout', views.logout_user, name="Logout | Neuron"),

    
]
