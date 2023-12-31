from rest_framework.routers import DefaultRouter

from eczmark.restful_api.viewsets  import (
    AnswerViewSet,
    QuestionViewSet,
    ReportViewSet,
    UserProfileViewSet,
)

router = DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='user')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'answers', AnswerViewSet, basename='answer')
router.register(r'reports', ReportViewSet, basename='report')

app_name = 'eczmark'
urlpatterns = router.urls
