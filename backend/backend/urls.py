"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from config.views import *

from posts.views import *


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'dashboard': reverse('dashboard', request=request, format=format),
        'logs': reverse('logs', request=request, format=format),
        'settings': reverse('settings', request=request, format=format),
        'users': reverse('users', request=request, format=format),
        'categories': reverse('categories', request=request, format=format),
        'regions': reverse('regions', request=request, format=format),
        'districts': reverse('districts', request=request, format=format),
        'posts': reverse('posts', request=request, format=format),
        'post-reactions': reverse('post-reactions', request=request, format=format),
        'comments': reverse('comments', request=request, format=format),
        'comment-reaction': reverse('comment-reaction', request=request, format=format),
    })


router = routers.DefaultRouter()
router.register(r'logs', LogViewSet)
router.register(r'settings', SettingViewSet)
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'posts', PostViewSet)
router.register(r'post-reactions', PostReactionViewSet)
router.register(r'comments', PostCommentViewSet)
router.register(r'comment-reaction', PostCommentReactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/config/district/<int:pk>', DistrictDetailView.as_view(), name='config_district_detail'),
    path('admin/config/region/<int:pk>', RegionDetailView.as_view(), name='config_region_detail'),
    path('admin/config/setting/<int:pk>', SettingDetailView.as_view(), name='config_setting_detail'),
    path('admin/config/log/<int:pk>', LogDetailView.as_view(), name='config_log_detail'),
    path('admin/config/customuser/<int:pk>', UserDetailView.as_view(), name='config_user_detail'),
    path('admin/config/category/<int:pk>', CategoryDetailView.as_view(), name='config_category_detail'),
    path('admin/config/post/<int:pk>', PostDetailView.as_view(), name='posts_post_detail'),
    path('admin/config/postcategory/<int:pk>', PostCategoryDetailView.as_view(), name='posts_postcategory_detail'),
    path('admin/config/post-comment/<int:pk>', PostCommentDetailView.as_view(), name='posts_postcomment_detail'),
    path('admin/', admin.site.urls),
]
