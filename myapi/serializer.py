from rest_framework import serializers
from .models import  Article, Post, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields = ('name','address')

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer( read_only=True)
    class Meta:
        model = Post
        fields = ('title' , 'text','author')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title','authors','email')
