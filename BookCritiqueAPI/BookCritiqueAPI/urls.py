from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews.views import ReviewViewSet

# Crea un enrutador y registra el conjunto de vistas
router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)

# Define las URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Esto incluye las rutas del enrutador
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
]

