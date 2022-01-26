from django.urls import path
from .views import home_view
app_name = 'store'
urlpatterns = [
    # reception url
    path('', home_view , name='home'),]
