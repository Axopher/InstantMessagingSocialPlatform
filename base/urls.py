# this is gonna be for specific app
# . meanings current directory


from django.urls import path
from . import views

# <str:pk> we are passing id into the url even though id is int but 
# since most people use string so str is used to target that pk or fk
urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),

    path('',views.home,name="home"),
    path('room/<str:pk>',views.room,name="room"),
    path('profile/<str:pk>',views.userProfile,name="user-profile"),
     # when someone go to our homepage we are gonna trigger home function
    path('create-room/',views.createRoom,name="create-room"),
    path('update-room/<str:pk>',views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>',views.deleteRoom,name="delete-room"),
    path('delete-message/<str:pk>',views.deleteMessage,name="delete-message"),
    path('update-user/',views.updateUser,name="update-user"),
    path('topics/',views.topicsPage,name="topics"),
    path('activity/',views.activityPage,name="activity"),
]
