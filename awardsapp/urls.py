from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name = 'indexpage'),
    path('accounts/profile/',views.profile,name = 'profile'),
    path(r'update_profile', views.update_profile, name='update'),
    path('project/<post>', views.project, name='project'),
    path(r'search/', views.search_results, name='search_results'),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/project/', views.PostList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)