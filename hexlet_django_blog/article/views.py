from django.shortcuts import render


# Create your views here.
def index(request):
    item = ['Articles']
    return render(
        request,
        'article/index.html',
        context={'info': item}
    )
