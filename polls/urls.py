from django.urls import path
from .views import index, detail_view, result_view, vote

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:request_id>', detail_view),
    path('result/<int:request_id>', result_view),
    path('vote/<int:request_id>', vote)
]