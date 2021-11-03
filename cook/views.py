from django.shortcuts import render
from django.views.generic import ListView

from cook.models import Post

# Create your views here.


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs("slug"))


        
def home(request):
    return render(request, 'base.html')