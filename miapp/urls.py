from django.urls import path
from .views import MedirTiempoRespuestaView

app_name="miapp"

urlpatterns = [
    path('', MedirTiempoRespuestaView.as_view(), name='medirTiempoRespuesta')
]
