from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.index , name = 'index'),
    path('update_emp/<emp_id>', views.update_emp , name = 'update_emp'),
    path('add_emp', views.add_emp , name = 'add_emp'),
    path('delete_emp/<int:emp_id>', views.delete_emp , name = 'delete_emp'),
    path('view_emp', views.view_emp , name = 'view_emp'),
]
