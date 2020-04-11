from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

def blog(request,*args,**kwargs):
    context={
      'posts':Post.objects.all()
    }
    return render(request,'index.html',context)
class PostListView(ListView):
    model=Post
    template_name ='index.html'#<app>/<model>_<viewtype>.html
    context_object_name ='posts'
    odering =['-date_posted']
class PostDetailView(DetailView):
     model=Post
     template_name='detail.html'
    #template_name ='index.html'
    #context_object_name ='posts'
    #odering =['-date_posted']
class PostCreate(LoginRequiredMixin,CreateView):
 model = Post
 fields=['title','content','author']
 template_name = 'update.html'
 def form_valid(self,form):
     form.instance.author = self.request.user
     return super().form_valid(form)

class PostUpdate(LoginRequiredMixin ,UserPassesTestMixin,UpdateView):
     model = Post
     fields = ['title', 'content', 'author']
     template_name = 'update.html'

     def form_valid(self, form):
         form.instance.author = self.request.user
         return super().form_valid(form)
     def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = Post
    template_name='delete.html'
    success_url='/blog'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
# template_name ='index.html'
# context_object_name ='posts'
# odering =['-date_posted']
 #class PostDetailView(DetailView):
  #   model=Post
   #  template_name='detail.html'
    #template_name ='index.html'
    #context_object_name ='posts'
    #odering =['-date_posted']

def about(request,*args,**kwargs):
    return render(request,'about.html')
