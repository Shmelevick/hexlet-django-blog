from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.views import View



# def index(request):
#     return render(
#         request,
#         "index.html",
#         context={
#             "who": "World",
#         },
#     )

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = "World"
        return context



def about(request):
    return render(request, "about.html")