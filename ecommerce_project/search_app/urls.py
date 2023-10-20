
from . import views
from django.urls import path
app_name='search_app'

urlpatterns = [

    path('',views.SearchResult,name='SearchResult'),
    # path('<slug:c_slug>/',views.SearchResult,name='result'),

]
