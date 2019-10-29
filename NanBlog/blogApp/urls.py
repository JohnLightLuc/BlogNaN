from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CategorieViewset, ArticleViewset, TagViewset, CommentaireViewset, ResponseCommentaireViewset, LikeViewset

router = DefaultRouter()
router.register(r'categorie', CategorieViewset, basename='categorie')
router.register(r'article', ArticleViewset, basename='article')
# router.register(r'archives', ArchiveViewset, basename='archives')
router.register(r'comment', CommentaireViewset, basename='comment')
router.register(r'responsecomment', ResponseCommentaireViewset, basename='responsecomment')
router.register(r'tag', TagViewset, basename='tag')
router.register(r'like', LikeViewset, basename='like')


from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('category/<str:idcat>',views.category,name='category'),
    path('single_blog/<str:idart>',views.single_blog,name='single_blog'),
    path('archive',views.archive,name='archive'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    re_path(r'^accounts/', include('allauth.urls')),
    ]
urlpatterns += router.urls

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'home'
