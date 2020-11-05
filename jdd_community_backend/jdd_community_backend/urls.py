from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from register import views as register_views
from register.views import CommunityCreateView

# To Do
# It should in different app
from . import views

urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('social-auth/', include('social_django.urls', namespace='social')),
    
    # To Do
    # It should in different app
    path('home/', views.home, name='home'), # redirect to user home after login
    path('login/', views.login, name='login'), # redirect to user home after login

    path('register/community/', CommunityCreateView.as_view(), name='register-community'), # register for pengurus komunitas
    path('register/manager/', register_views.create_manager, name='register-manager'), # register for pengurus komunitas

    path('event/', include('event.urls'))
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    try:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    except:
        pass
