from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from django_filters.rest_framework import DjangoFilterBackend

from .paginations import ProjectPagination, NewsPagination, GalleryPagination
from .tasks import send_email
from .models import Project, News, Gallery, Chronology, ProjectGallery, NewsGallery, GalleryFiles
from .serializers import (
    FeedbackCreateSerializer,
    ProjectListSerializer,
    ProductDetailSerializer,
    NewsListSerializer,
    NewsDetailSerializer,
    GalleryListSerializer,
    GalleryDetailSerializer,
    ChronologyDetailSerializer,
    ProjectGallerySerializer,
    NewsGallerySerializer,
    GalleryFilesSerializer
)


class HomePageView(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()[:7]
        news = News.objects.all()[:7]
        galleries = Gallery.objects.all()[:7]
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
            text = f'User: {request.data["name"]}\n' \
                   f'Phone: {request.data["phone"]}\n' \
                   f'Text: {request.data["message"]}'
            send_email.apply_async((text, ))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AboutPage(APIView):
    def get(self, request, *args, **kwargs):
        objects = Chronology.objects.all()
        if 'year' in self.request.query_params:
            objects = objects.filter(year=self.request.query_params['year'])
        serializer = ChronologyDetailSerializer(objects.first())
        return Response(serializer.data, status.HTTP_200_OK)


class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectListSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'body']
    filter_fields = ['region', 'type', 'is_finished']
    pagination_class = ProjectPagination

    def get_queryset(self):
        if 'old' in self.request.query_params:
            queryset = Project.objects.all().order_by('created')
        else:
            queryset = Project.objects.all()
        return queryset


class ProjectDetailView(APIView):
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        project_ser = ProductDetailSerializer(project)
        project_gallery = ProjectGallery.objects.filter(project=project)
        gallery_ser = ProjectGallerySerializer(project_gallery, many=True)
        return Response({
            'project': project_ser.data,
            'gallery': gallery_ser.data
        })


class NewsListView(generics.ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()
    pagination_class = NewsPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'short_description', 'body']


class NewsDetailView(APIView):
    def get(self, request, *args, **kwargs):
        object = get_object_or_404(News, pk=kwargs['pk'])
        object_serializer = NewsDetailSerializer(object)
        gallery = NewsGallery.objects.filter(news=object)
        gallery_ser = NewsGallerySerializer(gallery, many=True)
        if 'mobile' in self.request.query_params:
            return Response({'news': object_serializer.data, 'gallery': gallery_ser.data})
        else:
            news = News.objects.all()[:3]
            news_serializer = NewsListSerializer(news, many=True)
            return Response({
                'object_serializer': object_serializer.data,
                'news_serializer': news_serializer.data,
                'gallery': gallery_ser.data
            })


class GalleryListView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryListSerializer
    pagination_class = GalleryPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['is_photo']
    search_fields = ['title', 'body']


class GalleryDetailView(APIView):
    def get(self, request, *args, **kwargs):
        gallery = get_object_or_404(Gallery, pk=kwargs['pk'])
        gallery_ser = GalleryDetailSerializer(gallery)
        files = GalleryFiles.objects.filter(gallery=gallery)
        files_ser = GalleryFilesSerializer(files, many=True)
        return Response({
            'gallery': gallery_ser.data,
            'files': files_ser.data
        })
