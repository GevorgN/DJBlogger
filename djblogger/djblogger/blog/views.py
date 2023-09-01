from django.shortcuts import get_object_or_404, render

from django.views.generic import ListView
from djblogger.blog.models import Post


class HomeView(ListView):
	model = Post
	context_object_name = 'posts'
	paginate_by = 10

	def get_template_names(self):
		if self.request.htmx:
			return 'blog/components/post-list-elements.html'
		return 'blog/index.html'


def post_single(request, post):
	post = get_object_or_404(Post, slug=post, status='published')
	related = Post.objects.filter(author=post.author)[:5]
	return render(request, 'blog/single.html',{'post':post,'related':related})

def search_post(request):
	if request.method == 'POST':
		searched = request.POST.get('searched','')
		posts = Post.objects.filter(title__contains=searched)
		return render(request,'blog/search-post.html',{'posts':posts})