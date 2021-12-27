from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from django.urls.base import reverse
from .models import Post

class LatestPostsFeed(Feed):
    title = 'My Blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return truncatewords(item.body, 30)
        
    def item_link(self, item):
        return reverse('blog:post_detail', args=[
            item.created.year,item.created.month,item.created.day,item.slug])
