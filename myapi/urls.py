from django.urls import include, path
from .views import PostViewSet, ArticleViewSet, article_list, LogoutView
from rest_framework import routers, urlpatterns, views

router = routers.DefaultRouter()
router.register(r'Posts', PostViewSet)
router.register(r'article',ArticleViewSet)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('article/', include(router.urls) ),
    path('allow/',list),
    path('article_list/', article_list),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view()),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    
]
