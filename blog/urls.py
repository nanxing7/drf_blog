from django.urls import path

from blog import views

urlpatterns = [
    path('articles/', views.ArticleView.as_view(), name='index')
]
