from django.views.generic import CreateView
from django.urls import reverse_lazy

from blog.models import Blog


class BlogListView(CreateView):

    template_name = 'blog/blog_list.html'
    model = Blog
    fields = ['text']
    success_url = reverse_lazy('blog_list')

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['blog_list'] = Blog.objects.all()
        return context
