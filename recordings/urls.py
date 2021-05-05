from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name="Home Page"),
	path('dl',views.digitalLogic,name="digital logic"),
	path('c',views.c,name="C programming"),
	path('maths',views.maths,name="Maths"),
	path('iit',views.iit,name="IIT"),
	path('physics',views.physics,name="Physics"),
]