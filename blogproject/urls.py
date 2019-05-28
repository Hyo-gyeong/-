from django.contrib import admin
from django.urls import path, include
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/<int:blog_id>', blog.views.detail, name="detail"),
    path('api/', blog.views.api, name="api"),
    path('blog/new', blog.views.new, name="new"),
    path('blog/create', blog.views.create, name="create"),#path('어떤 url이 들어오면', (어디에 있는)어떤함수를 실행시켜라) 즉, views.py에 있는 create함수를 실행시켜라
    path('blog/edit/<int:blog_id>', blog.views.edit, name="edit"),
    path('blog/delete/<int:blog_id>', blog.views.delete, name="delete"),
    path('accounts/', include('allauth.urls')),
]
