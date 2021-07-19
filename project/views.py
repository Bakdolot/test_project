from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from django_filters.rest_framework import DjangoFilterBackend

from .paginations import ProjectPagination, NewsPagination, GalleryPagination
from .models import Project, News, Gallery
from .serializers import (
    FeedbackCreateSerializer,
    ProjectListSerializer,
    ProductDetailSerializer,
    NewsListSerializer,
    NewsDetailSerializer,
    GalleryListSerializer,
    GalleryDetailSerializer
)


class HomePageView(APIView):

    def get(self, request, format=None):
        projects = Project.objects.all()[:9]
        news = News.objects.all()[:9]
        galleries = Gallery.objects.all()[:9]
        project_serializer = ProjectListSerializer(projects, many=True)
        news_serializer = NewsListSerializer(news, many=True)
        gallery_serializer = GalleryListSerializer(galleries, many=True)
        return Response({
            'project_serializer': project_serializer.data,
            'news_serializer': news_serializer.data,
            'gallery_serializer': gallery_serializer.data,
        })

    def post(self, request, format=None):
        serializer = FeedbackCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectListSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'body']
    filter_fields = ['region', 'type', 'is_finished']
    pagination_class = ProjectPagination

    def get_queryset(self):
        try:
            re = self.request.query_params['old']
            queryset = Project.objects.all().order_by('created')
        except MultiValueDictKeyError:
            queryset = Project.objects.all()
        return queryset


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Project.objects.all()


class NewsListView(generics.ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()
    pagination_class = NewsPagination


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsDetailSerializer
    queryset = News.objects.all()


class GalleryListView(generics.ListAPIView):
    serializer_class = GalleryListSerializer
    pagination_class = GalleryPagination

    def get_queryset(self):
        try:
            video = self.request.query_params['video']
            queryset = Gallery.objects.filter(is_photo=False)
        except MultiValueDictKeyError:
            queryset = Gallery.objects.filter(is_photo=True)
        return queryset


class GalleryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GalleryDetailSerializer
    queryset = Gallery.objects.all()
