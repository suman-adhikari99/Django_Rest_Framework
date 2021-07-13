from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.serializers import Serializer
from django.http import HttpResponse, JsonResponse
from .serializer import ArticleSerializer, PostSerializer,AuthorSerializer
from .models import Post, Article, Author
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class= ArticleSerializer

@csrf_exempt
def article_list(request):

    if request.method == 'GET':
         articles = Article.objects.all()
         serializer= ArticleSerializer(articles,many=True)
         return JsonResponse(serializer.data, safe=False)


    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status = 400)

    

def article_detail(request,pk):
    try:
        article= Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method =="POST":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles)
        return JsonResponse(serializer.data, safe=False)

    elif request.mehtod=="PUT":
        pass


    
