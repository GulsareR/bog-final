from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('about/', views.about, name='about'),

    path('search/', views.search, name='search'),

    path('category/<slug:slug>/', views.postlist, name='postlist'),

    path('post/<slug:slug>/', views.post, name='post'),

    # Like / Unlike
    path('post/<slug:slug>/like/', views.like_post, name='like_post'),

    # Favorite / Unfavorite
    path('post/<slug:slug>/favorite/', views.favorite_post, name='favorite_post'),

    # Report / Şikayət
    path('post/<slug:slug>/report/', views.report_post, name='report_post'),

    # Taglara klik → postlar
    path('tag/<slug:slug>/', views.posts_by_tag, name='posts_by_tag'),

    # Bütün postlar
    path('allposts/', views.allposts, name='allposts'),
]


