from django.urls import path
from page_1 import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("update/<id>", views.update, name="update"),
    path("delete/<id>", views.deletedata, name="deletedata"),
]
