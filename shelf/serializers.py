from rest_framework import serializers
from .models import Book,Analytic,Reader,ShelfBook,Comment
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class LikesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytic
        fields = '__all__'

class SaveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'

class ShelfViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShelfBook
        fields = '__all__'

class CommentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BookDetailsSerializer(serializers.ModelSerializer):
    likes_per_book = serializers.IntegerField(source='number_of_likes_per_book',read_only=True)
    class Meta:
        model = Book
        fields = ('bookid','name','fileUrl','coverphoto','author','category','likes_per_book')
