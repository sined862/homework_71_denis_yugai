from urllib.parse import urlencode
from posts.models import Post, Comment
from accounts.models import Account
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View, ListView
from posts.forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, get_object_or_404
from posts.forms import SearchForm
from django.db.models import Q



class AccountsListView(ListView):
    template_name = 'accounts.html'
    model = Account
    context_object_name = 'accounts'

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        print(self.request.GET)
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)


    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None


    def get_queryset(self):
        queryset = super(AccountsListView, self).get_queryset()
        if self.search_value:
            query = Q(username__icontains=self.search_value) | Q(email__icontains=self.search_value) | Q(first_name__icontains=self.search_value)
            queryset = queryset.filter(query)
            print(queryset)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        return context


class IndexView(ListView):
    template_name = 'index.html'
    model = Post


    def get_context_data(self, **kwargs):
        form = SearchForm()
        context = super().get_context_data(**kwargs)
        posts_without_account = Post.objects.exclude(author=self.request.user.id)
        context['posts'] = posts_without_account
        context['search_form'] = form
        return context




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
            return redirect('post', pk=post_pk)
        return render(request, 'post_add.html', {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_form = SearchForm()
        context['search_form'] = search_form
        return context


class PostDetail(DetailView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'
    model_form = CommentForm
    
    def get_context_data(self, **kwargs):
        form = self.model_form()
        search_form = SearchForm()
        context = super().get_context_data(**kwargs)
        pk = self.object.id
        post = Post.objects.get(pk=pk)
        count = post.user_likes.all().count()
        account = Account.objects.get(pk=post.author_id)
        auth_account = Account.objects.get(pk=self.request.user.id)
        like_or_not = auth_account.liked_posts.filter(pk=pk)
        context['account'] = account.username
        context['count_likes'] = count
        context['like_or_not'] = like_or_not
        context['form'] = form
        context['search_form'] = search_form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if form.is_valid():
            Comment.objects.create(author=self.request.user, post=post, text=form.cleaned_data['text'])
            return redirect('post', pk=kwargs['pk'])
        return redirect('post', pk=kwargs['pk'])




class LikeView(View):
    def get(self, request, *args, **kwargs):
        account = Account.objects.get(pk=self.request.user.id)
        post = Post.objects.get(pk=kwargs['pk'])
        if account.liked_posts.filter(pk=kwargs['pk']):
            account.liked_posts.remove(post)
            return redirect('post', pk=kwargs['pk'])
        else:
            account.liked_posts.add(post)
            return redirect('post', pk=kwargs['pk'])


class AccountDetailView(DeleteView):
    template_name = 'account.html'
    model = Account
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        form = SearchForm()
        context['search_form'] = form
        count = Post.objects.filter(author=self.object.id).count()
        context['count'] = count
        posts = Post.objects.filter(author=self.object.id)
        context['posts'] = posts
        return context
        

# class CommentAddView(View):
    
#     def post(self, request, *args, **kwargs):
#         print(kwargs['pk'])
#         return redirect('post', pk=kwargs['pk'])
   