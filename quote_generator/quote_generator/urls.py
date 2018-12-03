from django.urls import include, path
from mainpage.views import main_page

urlpatterns = [
    path(r'^$', main_page(), name='main')
]
