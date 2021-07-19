from rest_framework.pagination import LimitOffsetPagination


class ProjectPagination(LimitOffsetPagination):
    default_limit = 9


class NewsPagination(LimitOffsetPagination):
    default_limit = 12


class GalleryPagination(LimitOffsetPagination):
    default_limit = 6
