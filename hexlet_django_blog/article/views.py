from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse
from django.views import View
from django.contrib import messages
from hexlet_django_blog.article.models import Article, Comment
from .forms import ArticleForm


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

class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/create.html", {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Статья успешно создана")
            return redirect('articles')
        messages.error(request, "Исправьте ошибки")
        return render(request, 'articles/create.html', {'form': form})

class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request,
            "articles/update.html",
            {'form': form, "article_id": article_id}
        )

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Статья успешно отредачена")
            return redirect("articles")
        
        messages.error(request, "Исправьте ошибки редактирования")
        return render(
            request,
            "articles/update.html",
            {'form': form, 'article_id': article_id}
        )
