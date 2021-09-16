from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Board, Rubric


def index(request):
    return render(request, 'board/index.html')


class BoardList(ListView):
    queryset = Board.objects.all()


class BoardDetail(DetailView):
    queryset = Board.objects.all()


class RubricDetail(DetailView):
    queryset = Rubric.objects.all()

class RubricList(ListView):
    queryset = Rubric.objects.all()
