"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path, include
from app01 import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('books', views.BooksViewSet)
# router.register('Students',views.StudentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^stu/(?P<pk>\d+)/',views.StuView.as_view()),
    re_path(r'^stus/$',views.StusView.as_view()),
    re_path(r'^sstu/$',views.SstuView.as_view()),
    re_path(r'^stu1/$',views.Stu1View.as_view()),
    re_path(r'^stu1/(?P<pk>\d+)',views.Stu1DetailView.as_view()),
    re_path(r'^stu2/',views.Stu2View.as_view()),
    re_path(r'^stu3/(?P<pk>\d+)',views.Stu3View.as_view()),
    re_path(r'stu4/$',views.Stu4View.as_view(actions={'get':'list','post':'create'})),
    re_path(r'stu4/(?P<pk>\d+)',views.Stu4View.as_view(actions={'get':'retrieve','put':'update','delete':'destroy'})),
    re_path(r'stu5/',views.Stu5Views.as_view(actions={'get':'get_all_stu'})),
]

# urlpatterns += router.urls
