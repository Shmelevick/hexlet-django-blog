from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse
from django.views import View
from hexlet_django_blog.article.models import Article, Comment

# Create your views here.

# def index(request):
#     name = "article"
#     return render(
#         request, 
#         "articles/index.html",
#         context={"name": name}
#     )

class ArticleIndexView(TemplateView):
    template_name = "articles/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.kwargs.get('tag')
        article_id = self.kwargs.get('article_id')
        context['name'] = 'ARTICLE'
        context['content'] = f"Статья номер {article_id}. Тег {tag}"
        return context


class HomeRedirectView(View):
    def get(self, request, *args, **kwargs):
        url = reverse('article', kwargs={"tag": "python", "article_id": 42})
        return redirect(url)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles
            }
        )

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )

class ArticleCommentsView(View): #todo
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(
            Comment, id=kwargs["id"], article__id=kwargs["article_id"]
        )
        return render(
            request,
            ""
        )
