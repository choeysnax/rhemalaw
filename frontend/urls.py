from django.urls import path

from frontend import views

app_name = 'frontend'
urlpatterns = [
    path('', views.index_view, name='home'),
    path('', views.index_view, name='index'),
    path('about', views.about_view, name='about'),
    path('insights', views.insights_view, name='insights'),
    path('contact', views.contact_view, name='contact'),
    path('areas-of-practice', views.areas_of_practice, name='areas_of_practice'),
    path('areas-of-practice/<slug:slug>', views.areas_of_practice, name='areas_of_practice'),
    path('team', views.rhema_team, name='rhema_team'),

]
