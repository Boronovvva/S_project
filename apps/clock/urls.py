from rest_framework.routers import DefaultRouter

from apps.clock.views import clockApi
from apps.users.views import UserAPI

router = DefaultRouter()
router.register('clock', clockApi, "api_clock"),
router.register('user', UserAPI , "api_user"),

urlpatterns = router.urls