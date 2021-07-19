from rest_framework import serializers

from .models import Feedback, Project, News, Gallery


class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'image', 'start_date', 'completion_date', 'region', 'project_number')


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'image', 'description', 'created')


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class GalleryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('title', 'image', 'created', 'is_photo')


class GalleryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
