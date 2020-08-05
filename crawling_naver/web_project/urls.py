"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from crawling.crawling_tasks import task_crawling_naver #빨래방 키워드
from crawling.crawling_tasks import task_crawling_naver2 

task_crawling_naver(schedule=10, repeat=3600) #실질적 time-set | delect from background_task &~completedtask (check)
task_crawling_naver2(schedule=10, repeat=3600)

urlpatterns = [
    path('admin/', admin.site.urls),
]
