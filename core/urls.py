from django.contrib import admin
from django.urls import path, include

urlpatterns = [
     path("calculator/", include("calculator.urls")),
     path("admin/", admin.site.urls),
]
