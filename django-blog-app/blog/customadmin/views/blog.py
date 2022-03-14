from django.shortcuts import redirect, reverse
from ..forms import PostCreationForm,PostUpdateForm
from .generic import MyDeleteView, MyDetailView, MyListView, MyUpdateView
from ..models import Post
from django.shortcuts import render


class PostListView(MyListView):
    model = Post
    template_name = "customadmin/post/post_list.html"
    context_object_name = 'post'
    
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