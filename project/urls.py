from django.urls import path

from .views import HomePageView, ProjectListView, ProductDetailView, NewsListView, NewsDetailView, GalleryListView, GalleryDetailView


urlpatterns = [
    path('', HomePageView.as_view()),
    path('project/', ProjectListView.as_view()),
    path('project/<int:pk>/', ProductDetailView.as_view()),
    path('news/', NewsListView.as_view()),
    path('news/<int:pk>/', NewsDetailView.as_view()),
    path('gallery/', GalleryListView.as_view()),
    path('gallery/<int:pk>/', GalleryDetailView.as_view())
]
