from inspect import classify_class_attrs

from customadmin.forms.category import CategoryUpdateForm
from ..forms import CategoryCreationForm
from django.shortcuts import reverse
from ..models import Category
from .generic import MyCreateView, MyDeleteView, MyDetailView, MyListView, MyUpdateView

class CategoryListView(MyListView):
    model = Category
    ordering = ['id']
    template_name = 'customadmin/category/category_list.html'
    context_object_name = 'category'

class CategoryCreateView(MyCreateView):
    model = Category
    form_class = CategoryCreationForm
    template_name = 'customadmin/category/category_create.html'

    def get_form_kwargs(self) :
        return super().get_form_kwargs()

    def get_success_url(self):
        return reverse('customadmin:category-list')

class CategoryDetailView(MyDetailView):
    model = Category
    template_name = 'customadmin/category/categroy_detail.html'
    context_object_name = "category"

class CategoryUpdateView(MyUpdateView):
    model = Category
    form_class = CategoryUpdateForm
    template_name = 'customadmin/category/category_update.html'

    def get_success_url(self):
        return reverse('customadmin:category-list')

class CategoryDeleteView(MyDeleteView):
    model = Category
    template_name = 'customadmin/confirm_delete.html'

    def get_success_url(self):
        return reverse('customadmin:category-list')