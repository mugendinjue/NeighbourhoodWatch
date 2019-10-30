from django.urls import path,re_path
from . import views as main_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('',main_views.homepage,name='homepage'),
  path('signup/',main_views.signup,name='signup'),
  path('login/',auth_views.LoginView.as_view(template_name = 'auth/login.html'),name='login'),
  path('logout/',auth_views.LogoutView.as_view(template_name = 'auth/logout.html'),name='logout'),
  path('profile/',main_views.profile,name='profile'),
  re_path(r'^new/neighbourhood/(?P<user_id>\d+)$',main_views.newHood,name='newHood'),
  re_path(r'^new/business/(?P<user_id>\d+)$',main_views.newbiz,name='newbiz'),
  path('hoods/',main_views.hoods,name='allhoods'),
  re_path(r'^join/(?P<hood_id>\d+)/(?P<user_id>\d+)$',main_views.joinhood,name='joinhood'),
  re_path(r'^Myhood/$',main_views.myhood,name='myhood'),
  re_path(r'^new/health/(?P<hood_id>\d+)$',main_views.healthContact,name='healthContact'),
  re_path(r'^new/security/(?P<hood_id>\d+)$',main_views.securityContact,name='securityContact'),
  re_path(r'^new/post/(?P<hood_id>\d+)/(?P<user_id>\d+)$',main_views.newpost,name='newpost'),
  path('search/',main_views.search,name='search'),

]

if settings.DEBUG:
  urlpatterns += static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
  )