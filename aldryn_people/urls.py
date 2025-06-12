from django.urls import path, re_path

from aldryn_people.views import DownloadVcardView, GroupDetailView, GroupListView, PersonDetailView


urlpatterns = [
    path('group/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    re_path(r'^group/(?P<slug>[A-Za-z0-9_\-]+)/$', GroupDetailView.as_view(), name='group-detail'),

    path('<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
    re_path(r'^(?P<slug>[A-Za-z0-9_\-]+)/$', PersonDetailView.as_view(), name='person-detail'),

    path('<int:pk>/download/', DownloadVcardView.as_view(), name='download_vcard'),
    re_path(r'^(?P<slug>[A-Za-z0-9_\-]+)/download/$', DownloadVcardView.as_view(), name='download_vcard'),

    path('', GroupListView.as_view(), name='group-list'),
]
