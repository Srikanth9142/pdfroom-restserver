from django.urls import path
from . import views
urlpatterns=[
    path('home',views.home,name="home"), #shelf/home
    path('list',views.BookList.as_view(),name="list_books"), #shelf/list
    path('like',views.SaveLike.as_view(),name="save like"),
    path('saveuser',views.SaveUser.as_view(),name="save user"), 
    path('getlike/<str:token>',views.ViewPersonLike.as_view(),name="get likes"),
    path('getuser/<str:token>',views.GetUserProfile.as_view(),name="get userprofile")
]