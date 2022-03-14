from dataclasses import field
from blogapp.models import Post
from django import forms


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        # fields = [
        #     'title'
        # ]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super(PostCreationForm,self).clean()
        print(cleaned_data)
        title = cleaned_data.get('title')    
        content = cleaned_data.get('content')    
        category = cleaned_data.get('category')
        post_image = cleaned_data.get('post_image')    

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super(PostUpdateForm,self).clean()
    
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance