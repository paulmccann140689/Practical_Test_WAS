from django.shortcuts import render
from newsapp.models import News


def index(request):

    news_List = News.objects.all()

    context_dict = {}
    context_dict['news'] = news_List
    return render(request, 'newsapp/index.html', context=context_dict)



