from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin, name='admin'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('submit', views.submit, name='submit'),
    path('admin_logut', views.admin_logut, name='admin_logut'),
    path('create_user', views.create_user, name='create_user'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('submit_edit/<int:id>', views.submitedit, name='submit_edit'),
    path('delete/<int:id>', views.delete, name='delete')
]
