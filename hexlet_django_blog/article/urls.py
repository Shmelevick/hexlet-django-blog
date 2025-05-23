from django.urls import path
from hexlet_django_blog.article.views import ArticleIndexView

urlpatterns = [
    path("<str:tag>/<int:article_id>/",
    ArticleIndexView.as_view(),
    name="article")
]
