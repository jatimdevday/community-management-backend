from django.urls import path

from . import views

urlpatterns = [
    # / : endpoint
    path('', views.EventEndpoint.as_view(), name='event'),
    # /view
    # path('list', views.EventList.as_view(), name='event-list'), # not yet implemented
    # /view/<id>
    # path('detail/<id>', views.EventDetail.as_view(), name='event-detail'), # not yet implemented
    # /new
    path('create', views.EventCreate.as_view(), name='event-create'),
    # /edit/<id>
    # path('update/<pk>', views.EventUpdate.as_view(), name='event-update'), # not yet implemented
]