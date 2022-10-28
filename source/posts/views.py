from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View, ListView
from posts.forms import PostForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render



class IndexView(ListView):
    template_name = 'index.html'
    model = Post


class PostAddView(LoginRequiredMixin, CreateView):
    template_name = 'post_add.html'
    form_class = PostForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = self.request.user
            instance.save()
            post = Post.objects.last()
            post_pk = post.id
            return reverse('post', kwargs={'pk': post_pk})
        return render(request, 'post_add.html', {'form': form})

    # def get_success_url(self):
    #     print(f"Это Pk - {self.object.pk}")
    #     return reverse('post', kwargs={'pk': self.object.pk})


class PostDetail(DetailView):
    template_name = 'post.html'
    model = Post

    
   