"""Back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.author.views import AuthorViewSets
from apps.video.views import VideoViewSets
from apps.auth.views import LoginViewSets, RegisterViewSets
from apps.auth.verify import CreateVerifyCode
from apps.message.views import MessageViewSets
from apps.chart.views import ChartViewSets
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPICodec


schemas_view = get_schema_view(title='API', renderer_classes=[SwaggerUIRenderer, OpenAPICodec])
Verify = CreateVerifyCode()
# router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'author', AuthorViewSets, base_name='author')
# router.register(r'video', VideoViewSets, base_name='video')

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^docs', schemas_view, name='docs'),
    # url(r'^', include(router.urls)),
    url(r'^author$', AuthorViewSets.as_view(), name='author'),
    url(r'^video$', VideoViewSets.as_view(), name='video'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login$', LoginViewSets.as_view(), name='login'),
    url(r'^register$', RegisterViewSets.as_view(), name='register'),
    url(r'^verify$', Verify.verify_code, name='verify'),
    url(r'^message$', MessageViewSets.as_view(), name='message'),
    url(r'^chart$', ChartViewSets.as_view(), name='chart')
]
