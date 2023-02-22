from django.urls import re_path
from dv_user import views

urlpatterns = [
    re_path(r'^books/',views.BookView.as_view()),
]
