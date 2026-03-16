from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView


from .models import Category, ListObject
from .forms import CategoryForm, ListObjectForm


class CategoryCreateView(LoginRequiredMixin, CreateView):

    model = Category
    form_class = CategoryForm
    template_name = "tasks/category_form.html"

    success_url = reverse_lazy("category_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CategoryListView(LoginRequiredMixin, ListView):

    model = Category
    template_name = "tasks/category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)

class CategoryDeleteView(LoginRequiredMixin, DeleteView):

    model = Category
    template_name = "tasks/category_confirm_delete.html"
    context_object_name = "category"

    def get_success_url(self):
        return reverse_lazy("category_list")
    
    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)
    
class CategoryDetailView(LoginRequiredMixin, DetailView):

    model = Category
    template_name = "tasks/category_detail.html"
    context_object_name = "category"

class ListObjectCreateView(LoginRequiredMixin, CreateView):

    model = ListObject
    form_class = ListObjectForm
    template_name = "tasks/object_form.html"

    def form_valid(self, form):

        form.instance.owner = self.request.user
        form.instance.category_id = self.kwargs["pk"]

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("category_detail", kwargs={"pk": self.kwargs["pk"]})
    
class ListObjectDeleteView(LoginRequiredMixin, DeleteView):

    model = ListObject
    template_name = "tasks/object_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy(
            "category_detail",
            kwargs={"pk": self.object.category.id}
        )