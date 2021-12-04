from django.urls import path,re_path
from .views import postsave,postlist,postDetails

urlpatterns = [
    path('post-list/', postlist, name='post-list'),
    path('post-save/', postsave, name='post_save'),
    #path('detail/<slug:slug>/', postDetails, name='post_detail'),
    re_path(r'(?P<slug>[-\w]+)/', postDetails,name='post_detail'),
]