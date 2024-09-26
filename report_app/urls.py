from django.urls import path

from . import views

urlpatterns = [
    path("report/", views.report, name="report"),
    path("capital_goods/", views.capital_goods, name="capital_goods"),
]