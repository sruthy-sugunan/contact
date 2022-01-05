from django.urls import path
from .import views

urlpatterns = [
    path('',views.homee,name='homee'),
	path('accounts/login/',views.loginview,name="login"),
	path('logout',views.logout_view),
    path('accounts/sign_up/',views.sign_up,name="signup") ,
	path('reset',views.Resethome,name='reset'), 
	path('passwordreset',views.resetPassword,name='resetpassword'),
    path('index',views.index,name='index'),
    path('hom',views.hom,name='hom'),
    path('view',views.view,name='view'),
    path('home',views.home,name='home'),
    path('up',views.update,name='up'),
    path('nameup',views.nameupdate,name='nameupdate'),
    path('numup',views.numupdate,name='numupdate'),
    path('dele',views.dele,name='dele'),
    path('delete',views.delete,name='delete')


]