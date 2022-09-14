
from django.urls import path
from . import views  # import menem


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name="about")    #ba path-i about link memonem  +  baroi ivazkunii link ex: (path('about123', views.about, name="about"))
]
