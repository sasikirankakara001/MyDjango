from django.urls import path,include
from Hero import views


urlpatterns = [

path('',views.index,name='index'),
path('Contact/',views.Contacts,name='Contact'),
path('Show/',views.Show,name='Show'),
path('Edit/<int:id>',views.Edit,name='edit'),
path('Delete/<int:id>',views.delete,name='delete'),
# path('display/',views.display,name='display'),
# path('modify/<int:id>',views.modify,name='modify'),


path('RegShow/',views.RegShow,name='RegShow'),
path('RegForm/',views.RegForm,name='RegForm'),
path('loginPage/',views.loginPage,name='loginPage'),





















]