from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('alunos.urls')),
    path('api/', include('disciplinas.urls')),
    path('api/', include('avaliacoes.urls')),
]