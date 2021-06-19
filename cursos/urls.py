from django.urls import path
from .views import (
    CursosApiView,
    AvaliacoesApiView,
    CursoApiView,
    AvaliacaoApiView,
    CursoViewSet,
    AvaliacaoViewSet)

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/', CursosApiView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoApiView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesApiView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoApiView.as_view(), name='curso_avaliacao'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoApiView.as_view(), name='avaliacao'),
    path('avaliacoes/', AvaliacoesApiView.as_view(), name='avaliacoes'),

]
