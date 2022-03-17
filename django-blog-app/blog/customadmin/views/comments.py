from customadmin.forms import comment
from customadmin.forms.comment import CommentCreateForm
from ..models import Comment
from .generic import MyCreateView, MyDeleteView, MyListView,MyDetailView, MyUpdateView
from ..forms import CommentUpdateForm
from django.shortcuts import reverse

class CommentListView(MyListView):
    model = Comment
    template_name = 'customadmin/comment/comment_list.html'
    context_object_name = "comment"
    ordering = ['-upload_on']

class CommentDetailView(MyDetailView):
    model = Comment
    template_name = 'customadmin/comment/comment_detail.html'
    context_object_name = 'comment'
class CommentUpdateView(MyUpdateView):
    model = Comment
    template_name = 'customadmin/comment/comment_update.html'
    form_class = CommentUpdateForm

    def get_success_url(self):
        return reverse('customadmin:comment-list')

class CommentDeleteView(MyDeleteView):
    model = Comment
    template_name = 'customadmin/confirm_delete.html'

    def get_success_url(self):
        return reverse('customadmin:comment-list')

class CommentCreateView(MyCreateView):
    model = Comment
    template_name = "customadmin/comment/comment_create.html"
    form_class = CommentCreateForm

    def get_form_kwargs(self):
        return super().get_form_kwargs()

    def get_success_url(self):
        return reverse("customadmin:comment-list")