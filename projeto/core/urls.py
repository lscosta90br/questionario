from django.urls import path
# from projeto.core import views as v
from . import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('pergunta/', v.PerguntaList.as_view(), name='pergunta_list'),
    # path(''pergunta/<int:pk>/', v.produto_detail, name='produto_detail'),
    # path(''pergunta/add/', v.ProdutoCreate.as_view(), name='produto_add'),
    # path(''pergunta/<int:pk>/edit/', v.ProdutoUpdate.as_view(), name='produto_edit'),
]