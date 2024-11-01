from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Register.as_view(), name='login'),
]+static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
