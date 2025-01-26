from django.contrib import admin
from django.urls import path, include

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
=======
    path('', include('app.urls')),
    path('admin/', admin.site.urls),

>>>>>>> 99fd0ab869c0cdfd9b146f3a3b0f1108d21af5d3
]
