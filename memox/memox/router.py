from memox_app.viewsets import MemoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('memo',MemoViewset)
