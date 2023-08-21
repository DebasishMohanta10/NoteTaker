from django.urls import path
from . import views
urlpatterns = [
    path("",views.notes,name="notes"),
    path("create/",views.create,name="create"),
    path("<int:noteId>/destroy/",views.destroy,name="destroy"),
    path("<int:noteId>/update/",views.update,name="update"),
]