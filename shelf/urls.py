from django.urls import path
from . import views
urlpatterns=[
    path('home',views.home,name="home"), #shelf/home
    path('list',views.BookList.as_view(),name="list_books"), #shelf/list
    path('like',views.SaveLike.as_view(),name="save like"),
    path('saveuser',views.SaveUser.as_view(),name="save user"), 
    path('savetoshelf',views.SaveToShelf.as_view(),name="save to shelf"),
    path('getlike/<str:token>',views.ViewPersonLike.as_view(),name="get likes"),
    path('getshelf/<str:token>',views.ViewPersonShelf.as_view(),name="get shelf books"),
    path('getuser/<str:token>',views.GetUserProfile.as_view(),name="get userprofile"),
    path('checksession/<str:token>',views.CheckSession.as_view(),name="user session"),
    path('viewcomments/<str:book_id>',views.ViewComments.as_view(),name="view comments"),
    path('addcomment',views.AddComment.as_view(),name="Add comment"),
    path('viewbook/<str:book_id>',views.GetDetailsOfBook.as_view(),name="Book Details"),
    path('addupvote',views.UpvoteReview.as_view(),name="Add upvote")
]