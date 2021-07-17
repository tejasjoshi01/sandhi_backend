from .views import LabourViewSet, SkillBasedLabourListViewSet , LocationSkillBasedJobListViewSet, JobViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path


router = DefaultRouter()
router.register('', LabourViewSet, basename="labour")


urlpatterns = [
    path('candidates/<skill>/', SkillBasedLabourListViewSet.as_view()),
    path('jobs/<location>/<skill>/', LocationSkillBasedJobListViewSet.as_view()),
    path('jobs/', JobViewSet.as_view({'get': 'list'})) ,
    path('jobs/register/', JobViewSet.as_view({'post': 'create'}))
]

urlpatterns += router.urls



