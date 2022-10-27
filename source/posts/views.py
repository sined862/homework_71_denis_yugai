from django.views.generic import ListView
from posts.models import Post
from instagram.settings import MEDIA_ROOT



class IndexView(ListView):
    template_name = 'index.html'
    model = Post
   