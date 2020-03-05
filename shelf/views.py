from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import Book,Analytic,Reader
from .serializers import BookSerializer,LikesViewSerializer,SaveUserSerializer,UserProfileSerializer
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
        book_temp.likes = book_temp.likes+1
        book_temp.save()
        user_email = RetrieveEmail(request.data.get('id_token'))
        analyticObj = Analytic(bookid=book_temp,email=user_email)
        analyticObj.save()
        print("saved like")
        return Response("good")

class ViewPersonLike(generics.ListAPIView):
    serializer_class = LikesViewSerializer

    def get_queryset(self):
        user_email = RetrieveEmail(self.kwargs['token'])
        return Analytic.objects.filter(email = user_email)

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

