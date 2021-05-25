"""murekkepvekeci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls import include

from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

from keci import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name="logout"), #aslında burada herhangi bir template sağlamamıza gerek yok -hatta sağlamamalıyız ki bu url'e gidildiğinde herhangi bir sayfa açılmasın- çünkü 'logout' yapanları doğrudan 'keci_home'a yönlendiriyoruz.
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name="password_change"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name="password_change_done"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path('password_reset/confirm/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirn.html'), name="password_reset_confirm"),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html')),
    path('keci/', include('keci.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)