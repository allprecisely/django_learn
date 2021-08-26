from django.urls import path

from blog import views

app_name = "blog"
urlpatterns = [
    path("", views.show_articles, name="show_articles"),
    path("<int:_id>/", views.show_article, name="show_article"),
    path("<int:_id>/update/", views.update_article, name="update_article"),
    path("create/", views.create_article, name="create"),
]
