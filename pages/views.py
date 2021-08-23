import datetime

from django.shortcuts import render


def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello World</h1>')
    context = {
        "user": request.user,
        "date": datetime.datetime.now(),
        "collection": ["pages", "products"],
        'html': '<p>Here is example of safe filter: HTML</p>',
    }
    return render(request, "home.html", context)
