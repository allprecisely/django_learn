from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View
from django.views import generic

from .models import Courses


class CoursesView(View):
    template_name = 'courses/courses_detail.html'

    def get(self, request, _id=None, *args, **kwargs):
        context = {}
        if _id:
            obj = get_object_or_404(Courses, id=_id)
            context['obj'] = obj
        return render(request, self.template_name, context)

# and so on

# class List(generic.ListView):
#     queryset = Courses.objects.all()
