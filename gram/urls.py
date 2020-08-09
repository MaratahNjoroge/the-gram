from django.conf.urls import url,include
from .views import (
    PostListView
)
    

app_name = 'gram'
urlpatterns=[
    url('^$',PostListView.as_view(),name = 'post'),
]