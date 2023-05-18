from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.Article.main, name='main'),
    path('<str:tags>/<int:article_id>/', views.Article.index, name='article'),
]
