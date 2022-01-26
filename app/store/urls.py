from django.urls import path
from .views import book_detail_view, home_view
app_name = 'store'
urlpatterns = [
    # reception url
    path('', home_view , name='home'),
    path('book/<int:id>', book_detail_view)
    ]
