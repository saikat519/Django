from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name = 'index'),
    path('home/',views.home,name = 'home'),
    path('details/<int:id>',views.detail_view,name='details'),
    path('update/<int:id>',views.update_post,name='update'),
    path('delete/<int:id>',views.delete_post,name='delete'),
    path('view/',views.form_view,name='view'),

]