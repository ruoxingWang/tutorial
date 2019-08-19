from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = [
    # url(r'^snippet/$', views.snippet_list),
    # url(r'^snippet/(?P<pk>[0-9]+)/$', views.snippet_detail),
    # url(r'^snippet/$', views.SnippetList.as_view()),
    # url(r'^snippet/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^snippet/$', views.SnippetListByView.as_view()),
    url(r'^snippet/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]


