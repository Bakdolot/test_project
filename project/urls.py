from django.urls import path

from .views import (
    HomePageView,
    ProjectListView,
    ProjectDetailView,
    NewsListView,
    NewsDetailView,
    GalleryListView,
    GalleryDetailView,
    AboutPage
)


urlpatterns = [
    path('', HomePageView.as_view()),
    path('about_as/', AboutPage.as_view()),
    path('project/', ProjectListView.as_view()),
    path('project/<int:pk>/', ProjectDetailView.as_view()),
    path('news/', NewsListView.as_view()),
    path('news/<int:pk>/', NewsDetailView.as_view()),
    path('gallery/', GalleryListView.as_view()),
    path('gallery/<int:pk>/', GalleryDetailView.as_view())
]
