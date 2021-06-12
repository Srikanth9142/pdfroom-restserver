from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import Book,Analytic,Reader,ShelfBook,Comment
from .serializers import (BookSerializer,LikesViewSerializer,SaveUserSerializer,
                            UserProfileSerializer,ShelfViewSerializer,CommentViewSerializer,BookDetailsSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from .checkserver import RetrieveUserInfo,RetrieveEmail

def home(request):
    return HttpResponse("neeku ardamavutundaa")

class BookList(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAdminUser]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SaveLike(APIView):
    def post(self,request):
        #print("got data ",email,bookid)
        #print(request.body)
        book_temp = Book.objects.get(bookid=request.data.get('bookid'))
        # book_temp.likes = book_temp.likes+1
        #book_temp.save()
        user_email = RetrieveEmail(request.data.get('id_token'))
        if(Analytic.objects.filter(email=user_email,bookid=book_temp)):
            print("Duplicate record")
        else:
            analyticObj = Analytic(bookid=book_temp,email=user_email)
            analyticObj.save()
            print("saved like")
        return Response("good")

class SaveToShelf(APIView):
    def post(self,request):
        book_obj = Book.objects.get(bookid=request.data.get('bookid'))
        user_email = RetrieveEmail(request.data.get('id_token'))
        if(ShelfBook.objects.filter(email=user_email,bookid = book_obj)):
            print("duplicate record")
        else:
            shelfobj = ShelfBook(bookid = book_obj,email = user_email)
            shelfobj.save()
            print("added to shelf")
        return Response("saved")

class ViewPersonLike(generics.ListAPIView):
    serializer_class = LikesViewSerializer

    def get_queryset(self):
        user_email = RetrieveEmail(self.kwargs['token'])
        return Analytic.objects.filter(email = user_email)

class ViewPersonShelf(generics.ListAPIView):
    serializer_class = ShelfViewSerializer

    def get_queryset(self):
        user_email = RetrieveEmail(self.kwargs['token'])
        return ShelfBook.objects.filter(email = user_email)

class SaveUser(APIView):
    serializer_class = SaveUserSerializer

    def post(self,request):
        readerinstance = Reader()
        useremail,name,photoid = RetrieveUserInfo(request.data.get('id_token'))
        if(Reader.objects.filter(email=useremail).exists()):
            print("user exist")
            return Response("user exist")
        else:
            Readerobj = Reader(email=useremail,name=name,photoid=photoid)
            Readerobj.save()
            #print(Readerobj)
            print("user saved")
            return Response("user saved")

class GetUserProfile(generics.ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        user_email = RetrieveEmail(self.kwargs['token'])
        return Reader.objects.filter(email=user_email)


#working fine checked with postman
class CheckSession(APIView):
    def get(self,request,token):
        if(RetrieveEmail(token)=="Token expired"):
            return Response({"result":"session expired"},status=200)
            #return Response("session expired")
        else:
        #return Response({"result":"Active session"},status=200)
            return Response({"result":"active session"},status=200)
        return HttpResponse("ok")

# Adding comments view
class ViewComments(generics.ListAPIView):
     serializer_class = CommentViewSerializer

     def get_queryset(self):
         book_id = self.kwargs['book_id']
         return Comment.objects.filter(bookid=book_id)


class AddComment(APIView):
    def post(self,request):
        
        book_id = request.data.get('bookid')
        message = request.data.get('message')
        comment_id = request.data.get('comment_id')
        print("message: ",message)
        print("commentId: ",comment_id)
        user_email =  RetrieveEmail(request.data.get('id_token'))
        print(user_email)
        user_obj = Reader.objects.get(email=user_email)
        user_name = user_obj.name
        book_instance = Book.objects.get(bookid=book_id)
        comment_obj = Comment(comment_id=comment_id,bookid=book_instance,email=user_email,user_name=user_name,message=message)
        comment_obj.save()
        return Response("Comment added")

class GetDetailsOfBook(generics.ListAPIView):
    serializer_class = BookDetailsSerializer

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Book.objects.filter(bookid=book_id)

class UpvoteReview(APIView):
    def post(self,request):
        print("upvote called")
        comment_obj = Comment.objects.get(comment_id=request.data.get('comment_id'))
        reader_obj = Reader.objects.get(email=comment_obj.email)
        reader_obj.points +=1
        comment_obj.upvotes += 1
        comment_obj.save()
        reader_obj.save()
        return Response("Upvote added")