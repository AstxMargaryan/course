from django.urls import path
from . import views

app_name = "models"
urlpatterns = [
    path("", views.first, name='all_courses'),
    path("<int:course_id>/", views.detail, name='course_detail'),
    path('rate/', views.rate_course, name='rate_course'),
]

