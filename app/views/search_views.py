from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from ..models import Tarefa

def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = Tarefa.objects.filter(Q(fornecedor__icontains=srch)|
                    Q(produto__icontains=srch)
                    )
            if match:
                return render(request, "tarefas/search.html", {"sr": match})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request, 'tarefas/search.html')