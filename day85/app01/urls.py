
from django.urls import re_path

from app01 import views

urlpatterns = [
    re_path('^books/',views.BookAPIView.as_view()),
    re_path('^book/(?P<pk>\d+)',views.BookAPIView.as_view()),
    re_path('^book2/',views.BookView.as_view()),
]
