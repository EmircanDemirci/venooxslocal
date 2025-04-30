from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.views.generic.detail import DetailView

def index_view(request):
    posts = Post.objects.all().order_by('-created_at')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({"posts":posts},request))

class PostView(DetailView):
    model = Post
    template_name = 'detailview.html'

#add index view
#blog post section users only see posts
#add views for each post