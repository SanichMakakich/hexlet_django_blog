from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse

# from django.http import HttpResponse


# Create your views here.

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
