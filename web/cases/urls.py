from django.urls import path
from . import views

app_name = "cases"
urlpatterns = [
    path("<int:ref_id>/", views.case_detail_view, name="case_detail"),
    path("list/", views.case_list_view, name="cases_list"),
    path("create/", views.case_create_view, name="case_create"),
]
