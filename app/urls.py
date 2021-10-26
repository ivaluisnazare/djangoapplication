from django.urls import path
from .views.graphy_views import *
from .views.tarefa_views import *
from .views.usuario_views import *
from .views.search_views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index_tarefas/', index_tarefas, name='index_tarefas'),
    path('listar_tarefas/', listar_tarefas, name='listar_tarefas'),
    path('cadastrar_tarefa/', cadastrar_tarefa, name='cadastrar_tarefa'),
    path('editar_tarefa/<int:id>', editar_tarefa, name='editar_tarefa'),
    path('remover_tarefa/<int:id>', remover_tarefa, name='remover_tarefa'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),
    path('grid_plot/', grid_plot, name='grid_plot'),
    path('search/', search, name='search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


