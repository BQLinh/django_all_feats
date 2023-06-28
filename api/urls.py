from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("bye", views.User.as_view({'get': 'list'}), name='tom'),
    path("delete", views.User.as_view({'delete': 'delete'}), name='linh')
]