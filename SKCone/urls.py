"""SKCone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from skcone_web import views
from django.conf import settings
from django.conf.urls.static import static
from ms_identity_web.django.msal_views_and_urls import MsalViews

msal_urls = MsalViews(settings.MS_IDENTITY_WEB).url_patterns()

urlpatterns = [
    path('admin/', admin.site.urls),   
    path('', views.login,name="login"),
    path('index', views.index,name="index"),
    # path('index\\Z', views.index,name="index"),
    path('sign_in_status', views.index, name='status'),
    path('token_details', views.token_details, name='token_details'),
    path('History', views.history, name='history'),
    path('Dashboard', views.dashboard, name='dashboard'),
    path('contact', views.contact, name='contact'),
    path('call_ms_graph', views.call_ms_graph, name='call_ms_graph'),

    path(f'{settings.AAD_CONFIG.django.auth_endpoints.prefix}/', include(msal_urls)),   # path(url sign_in จาก aad.config,เรียกฟังก์ชัน)
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),

    path('api/',views.apiList,name='api-list'),
    path('api/testRequest-list/', views.testRequestlist, name='todo-list'),
    path('api/testRequest-detail/<str:pk>/', views.testRequestdetail, name='task-detail'),
    path('api/testRequest-update/<str:pk>/',views.testRequestupdate,name='task-update'),
    path('api/chartSystems/', views.chartSystems, name='chartSystems'),
    path('api/chartDocstatus/', views.chartDocstatus, name='chartDocstatus'),
]
