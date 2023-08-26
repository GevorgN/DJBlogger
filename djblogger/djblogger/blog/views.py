from django.shortcuts import render

from django.views.generic import ListView
from djblogger.blog.models import Post


class HomeView(ListView):
	model = Post
	template_name = 'blog/index.html'
