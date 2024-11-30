from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ArticleViewSet,
    MultimediaViewSet,
    CommentViewSet,
    SearchView,
    AppConfigView,
    TokenObtainPairView,
    TokenRefreshView,
    RegisterView,
    LoginView,
)

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'multimedia', MultimediaViewSet, basename='multimedia')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('config/', AppConfigView.as_view(), name='app_config'),
    path('search/', SearchView.as_view(), name='search'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

urlpatterns += router.urls
