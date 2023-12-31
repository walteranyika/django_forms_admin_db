"""
URL configuration for customize_admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from customize_admin import settings
from main_app import views

urlpatterns = [
    path("", views.students, name="home"),
    path("employees/add", views.employee_add, name="employee.add"),
    path("employees", views.employees_view, name="employees.view"),
    path("students", views.students_view, name="students.view"),
    path("upload-images", views.upload_images, name="upload_images"),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Wezesha"
admin.site.index_title = "Wezesha Site Administration"
