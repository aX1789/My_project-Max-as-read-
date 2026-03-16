from django import forms
from .models import Category, ListObject


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "template"]


class ListObjectForm(forms.ModelForm):
    class Meta:
        model = ListObject
        fields = [
            "name",
            "status",
            "notes",
            "rating",
            "favorite",
            "started_at",
            "finished_at",
        ]
