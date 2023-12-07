from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostCreateForm
from .models import Post

# Create your views here.
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()

        context = {
            'posts': posts,
        }
        return render(request, 'blog_list.html', context)
    
class BlogCreateView(View):
    def get(self, request, *args, **kargs):
        form = PostCreateForm()
        context = {
            'form': form
        }
        return render(request, 'blog_create.html', context)     

    def post(self, request, *args, **kargs):
        if request.method == "POST":
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                ##Metodo de django '.objects.get_or_create()' busca atributo en el objeto o sino lo crea
                p, created = Post.objects.get_or_create(title=title, content=content)

                ## Metodo de django '.save()' guarda en BBDD
                p.save()
                
                return redirect('blog:home')
        context = {

        }
        return render(request, 'blog_create.html', context)
    
class BlogDetailView(View):
    def get(self, request, pk,*args, **kwargs):

        ## Obtiene objeto donde la primarykey = pk que viene por la url
        post = get_object_or_404(Post, pk=pk)

        context = {
            'post': post,
        }
        return render(request, 'blog_detail.html', context)
    
class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']

    template_name = 'blog_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk': pk})
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog:home')