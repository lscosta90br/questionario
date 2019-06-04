from django.contrib import admin
from projeto.core.models import Enquete, Pergunta, Resposta, PerguntaResposta, Prova
from django.utils import timezone

class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 0


class PerguntaAdmin(admin.ModelAdmin):
    # filter_horizonal = ('questionario',)
    list_display = ['descricao',]
    list_filter = ['descricao']
    search_fields = ['descricao']
    inlines = [
        RespostaInline,
    ]


class PerguntaInline(admin.TabularInline):
    model = Pergunta
    extra = 0

class PerguntaRespostaAdmin(admin.ModelAdmin):
    inlines = [
        PerguntaInline,
    ]

admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(PerguntaResposta, PerguntaRespostaAdmin)
admin.site.register(Enquete)
admin.site.register(Prova)
# admin.site.register(PerguntaResposta)
# admin.site.register(Pergunta)
# admin.site.register(Resposta)


