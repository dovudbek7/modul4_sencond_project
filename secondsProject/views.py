# blog/views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article, MultimediaContent, Comment
from .serializers import ArticleSerializer, MultimediaContentSerializer, CommentSerializer, RegisterSerializer, \
    UserSerializer, TokenSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['article_type', 'author']
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MultimediaViewSet(ModelViewSet):
    queryset = MultimediaContent.objects.all()
    serializer_class = MultimediaContentSerializer
    filterset_fields = ['content_type']
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = ['article', 'is_approved']


class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        if not query:
            return Response({"error": "Query parameter 'q' is required."}, status=400)

        articles = Article.objects.filter(title__icontains=query)
        multimedia = MultimediaContent.objects.filter(title__icontains=query)

        article_results = [{"id": a.id, "title": a.title, "type": "article"} for a in articles]
        multimedia_results = [{"id": m.id, "title": m.title, "type": m.content_type} for m in multimedia]

        return Response({
            "results": article_results + multimedia_results,
            "total_results": len(article_results) + len(multimedia_results),
        })


class AppConfigView(APIView):
    def get(self, request):
        config = {
            "articles_per_page": 10,
            "allowed_file_types": ["jpg", "png", "mp4", "mp3"],
            "max_file_size": 10485760,
        }
        return Response(config)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login View (JWT)
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response(TokenSerializer({'refresh': str(refresh), 'access': str(refresh.access_token)}).data)
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
