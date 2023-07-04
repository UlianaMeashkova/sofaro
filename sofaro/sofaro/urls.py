"""shop URL Configuration
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from products.views import hotels
from users.views import users, register, login_view, logout_view, countries, oneHotel, booking, goodBook, contacts, comment, leaveComment
# , contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls', namespace="api")),
    # path('api/auth/', include(
    #     'rest_framework.urls', namespace='rest_framework'
    # )),
    path('users/', users, name="users"),
    path('register/', register, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('hotels/<country>/', hotels, name="hotels"),
    path('hotel/<hotel_id>/', oneHotel, name="oneHotel"),
    path('', countries, name="index"),
    path('booking/', booking, name="booking"),
    path('goodBook/', goodBook, name="goodBook"),
    path('contacts/', contacts, name="contacts"),
    path('comment/<hotel_id>', comment, name="comment"),
    path('leaveComment/', leaveComment, name="leaveComment"),

]
 

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
