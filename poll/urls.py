from django.urls import path
from poll import views as poll_views


urlpatterns = [
    path('', poll_views.home, name='poll_home'),
    path('create', poll_views.create, name='poll_create'),
    path('vote/<poll_id>', poll_views.vote, name='poll_vote'),
    path('results/<poll_id>', poll_views.results, name="poll_results")
]