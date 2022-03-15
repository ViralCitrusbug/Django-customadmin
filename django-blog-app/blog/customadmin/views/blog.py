from django.db.models import Q
from django.views import View
from blogapp.models import Category
from customadmin.forms.post import PostToArchiveForm
from customadmin.mixins import HasPermissionsMixin
from ..views.generic import MyLoginRequiredView 
from django.shortcuts import redirect, reverse
from ..forms import PostCreationForm,PostUpdateForm
from .generic import MyCreateView, MyDeleteView, MyDetailView, MyListView, MyUpdateView
from ..models import Post
from django.shortcuts import render
from django_datatables_too.mixins import DataTableMixin
from django.template.loader import get_template


class PostListView(MyListView):
    model = Post
    ordering = ['-published_date']
    template_name = "customadmin/post/post_list.html"
    context_object_name = 'post'
    # paginate_by = 4

class PostCreateView(MyCreateView):
    model = Post
    form_class = PostCreationForm
    template_name = "customadmin/post/post_create.html"
    context = {}

    def get_form_kwargs(self) :
        return super().get_form_kwargs()

    def get_success_url(self):
        print("In Success Url")
        return reverse('customadmin:post-list')

class PostDetailView(MyDetailView):
    model = Post
    template_name = "customadmin/post/post_detail.html"
    context = {}

    def get(self, request, pk):
        self.context['post_detail'] = self.model.objects.filter(pk=pk).first()
        return render(request, self.template_name, self.context)

class PostDeleteView(MyDeleteView):
    model = Post
    template_name = 'customadmin/confirm_delete.html'

    def get_success_url(self):
        return reverse('customadmin:post-list')

class PostUpdateView(MyUpdateView):
    model = Post
    template_name = 'customadmin/post/post_update.html'
    form_class = PostUpdateForm

    def get_success_url(self):
        return reverse('customadmin:post-list')

class PostToArchive(MyUpdateView):
    model = Post
    template_name = "customadmin/post/post_to_archive.html"
    form_class = PostToArchiveForm

    def get_success_url(self):
        return reverse('customadmin:post-list') 

