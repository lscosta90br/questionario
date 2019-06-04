from django.shortcuts import render
from .models import Pergunta
from django.views.generic import CreateView, UpdateView, ListView

def index(request):
    return render(request, 'index.html')

class PerguntaList(ListView):
    model = Pergunta
    template_name = 'pergunta_list.html'
    # paginate_by = 10