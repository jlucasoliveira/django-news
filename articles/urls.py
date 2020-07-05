from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='update'),
    path('<int:pk>/detail/', views.ArticleDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='delete'),
    path('new/', views.ArticleCreateView.as_view(), name='create'),
    path('', views.ArticleListView.as_view(), name='index'),
]
