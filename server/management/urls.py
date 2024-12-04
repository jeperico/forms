from management import views
from django.urls import include, path
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'user', views.UserView)


urlpatterns = [
  path('', include(router.urls)),
]
