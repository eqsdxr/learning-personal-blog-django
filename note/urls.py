from django.urls import path

from . import views 

app_name = 'note'

urlpatterns = [
    path('<int:id>/', views.view_note, name='note')
]