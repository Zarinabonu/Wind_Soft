from django.urls import path, include

from api.post.views import PostCreate

urlpatterns = [
    path('create/', PostCreate.as_view(), name='api-create')
]