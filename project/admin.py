from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Feedback, Project, News, Gallery, Chronology, ProjectGallery, NewsGallery, GalleryFiles


class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery
    extra = 1
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = 'Изображение'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectGalleryInline]
    list_display = ['title', 'region', 'get_image']
    list_display_links = ['title']
    list_filter = ['region', 'is_finished', 'type']
    search_fields = ['title', 'body']
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = 'Изображение'


class NewsGalleryInline(admin.TabularInline):
    model = NewsGallery
    extra = 1
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = 'Изображение'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsGalleryInline]
    list_display = ['title', 'get_image']
    list_display_links = ['title']
    search_fields = ['title', 'body', 'short_description']
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = 'Изображение'


class GalleryFilesInline(admin.TabularInline):
    model = GalleryFiles
    extra = 1
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = 'Изображение'


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_photo', 'get_image']
    list_display_links = ['title']
    inlines = [GalleryFilesInline]
    list_filter = ['is_photo']
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = 'Изображение'


@admin.register(ProjectGallery)
class ProjectGalleryAdmin(admin.ModelAdmin):
    list_display = ['project', 'get_image']
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = 'Изображение'


@admin.register(NewsGallery)
class NewsGalleryAdmin(admin.ModelAdmin):
    list_display = ['news', 'get_image']
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = 'Изображение'


@admin.register(GalleryFiles)
class GalleryFilesAdmin(admin.ModelAdmin):
    list_display = ['gallery', 'get_image']
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = 'Изображение'


admin.site.register(Feedback)
admin.site.register(Chronology)
