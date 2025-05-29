from django.urls import path
from hexlet_django_blog.article.views import (
    ArticleIndexView,
    IndexView,
    ArticleView,
    ArticleCommentsView,
    ArticleFormCreateView
)

urlpatterns = [
    path("<str:tag>/<int:article_id>/",
    ArticleIndexView.as_view(),
    name="article"),
    path("", IndexView.as_view(), name='articles'),
    path("<int:id>/", ArticleView.as_view(), name='article_detail'),
    path('<int:article_id>/comments/<int:id>', ArticleCommentsView.as_view()),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]
