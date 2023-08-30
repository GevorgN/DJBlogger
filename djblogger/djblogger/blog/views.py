from django.shortcuts import render

from django.views.generic import ListView
from djblogger.blog.models import Post


class HomeView(ListView):
	model = Post
	context_object_name = 'posts'
	paginate_by = 10

	def get_template_names(self):
		if self.request.htmx:
			print("XXXXX")
			return 'blog/components/post-list-elements.html'
		return 'blog/index.html'


