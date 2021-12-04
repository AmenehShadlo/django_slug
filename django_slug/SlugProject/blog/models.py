from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200) #python learning
    slug = models.SlugField(unique=True,allow_unicode=True) #python-learning
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    content = models.TextField()
  
  
    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('post_detail' ,args=[self.slug])


    



