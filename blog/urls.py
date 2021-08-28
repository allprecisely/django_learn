from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article-update'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article-delete'),
    path('create/', views.ArticleCreateView.as_view(), name='article-create'),
]
