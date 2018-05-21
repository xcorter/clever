from django.shortcuts import render
from django.views import generic
from .models import Game, Question

class IndexView(generic.ListView):
    model = Game
    template_name = 'main/index.html'
    context_object_name = 'games'
    queryset = Game.objects.order_by('-date_time')
    paginate_by = 1

class GameDetailView(generic.DetailView):
    model = Game
    template_name = 'main/detail-game.html'
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)
        game = context['object']
        questions = Question.objects.filter(game=game)
        context['questions'] = questions
        return context
