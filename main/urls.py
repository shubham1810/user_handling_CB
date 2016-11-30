from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'users_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^data/', views.some_data, name='data'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^leaderboard/', views.leaderboard, name='leaderboard'),
)
