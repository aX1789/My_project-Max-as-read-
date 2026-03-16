from django.urls import path
from .views import CategoryCreateView, CategoryListView, CategoryDetailView, ListObjectCreateView, ListObjectDeleteView, CategoryDeleteView

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/create/", CategoryCreateView.as_view(), name="category_create"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("categories/<int:pk>/add/", ListObjectCreateView.as_view(), name="object_create"),
    path("objects/<int:pk>/delete/", ListObjectDeleteView.as_view(), name="object_delete"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category_delete"),
]