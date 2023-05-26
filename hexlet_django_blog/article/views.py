from django.shortcuts import render
from django.views import View

from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })


# Create your views here.
'''
class Article(View):

    def main(self):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 12}))

    def index(request, tags, article_id):
        item = ['Articles']
        return render(
            request,
            'article/index.html',
            context={'info': item,
                     'tags': tags,
                     'article_id': article_id}
        )
        # return HttpResponse(f'любая строка а так же любой{item}')
'''
