
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('Basquet2023_DatosApp/', include('Basquet2023_DatosApp.urls'))
]
