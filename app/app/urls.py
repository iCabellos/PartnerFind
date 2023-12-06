from django.contrib import admin
from django.urls import path, include
from PartnerFind.views import ContentView, CreateMatchView, CreateUser

urlpatterns = [
    path('', ContentView.as_view(), name='index'),
    path('new-match/', CreateMatchView.as_view(), name='create-match'),
    path('admin/', admin.site.urls),
    path('register/', CreateUser.as_view(), name='register'),
    path('accounts/', include('allauth.urls')),
]
