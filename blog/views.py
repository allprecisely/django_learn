# from django.shortcuts import get_object_or_404
# from django.shortcuts import redirect
# from django.shortcuts import render
from django.views import generic

from .forms import ArticleForm
from .models import Article


# def show_articles(request, *args, **kwargs):
#     objects = Article.objects.all()
#     if request.POST.get('create'):
#         return redirect('create/')
#     context = {'objects': objects}
#     return render(request, 'blog/main.html', context)
#
#
# def show_article(request, _id, *args, **kwargs):
#     print(dir(request))
#     obj = get_object_or_404(Article, id=_id)
#     if request.POST.get('delete'):
#         obj.delete()
#         return redirect('../')
#     if request.POST.get('update'):
#         return redirect('update/')
#     context = {'obj': obj}
#     return render(request, 'blog/article.html', context)
#
#
# def update_article(request, _id, *args, **kwargs):
#     obj = get_object_or_404(Article, id=_id)
#     if request.POST:
#         obj.title = request.POST.get('title')
#         obj.body = request.POST.get('body')
#         obj.author = request.POST.get('author')
#         # Can be added field edited with normal time
#         obj.save()
#         return redirect('../')
#     form = ArticleForm(obj.__dict__)
#     context = {'form': form}
#     return render(request, 'blog/update_article.html', context)
#
#
# def create_article(request, *args, **kwargs):
#     form = ArticleForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('../')
#     context = {'form': form}
#     return render(request, 'blog/create_article.html', context)


class ArticleCreateView(generic.CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()


class ArticleDetailView(generic.DetailView):
    queryset = Article.objects.all()


class ArticleDeleteView(generic.DeleteView):
    template_name = 'blog/article_delete.html'
    queryset = Article.objects.all()

    def get_success_url(self):
        return '/blog/'


class ArticleListView(generic.ListView):
    queryset = Article.objects.all()


class ArticleUpdateView(generic.UpdateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
