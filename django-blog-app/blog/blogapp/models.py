from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(default=now)
    post_image = models.ImageField(upload_to='post/post-image/',null=True)
    soft_delete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    
class Image(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/post-images')

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='user/profile/profile-pic')
    def __str__(self) -> str:
        return self.user.username

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)
    upload_on = models.DateTimeField(default=now)  

    def __str__(self) -> str:
        return f"{self.user.username}:-\t{self.comment[0:10]}..."

@receiver(post_save,sender=User)
def create_auth_token(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)