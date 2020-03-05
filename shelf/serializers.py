from rest_framework import serializers
from .models import Book,Analytic,Reader
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