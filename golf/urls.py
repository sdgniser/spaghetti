from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from .views import *

app_name = 'golf'
urlpatterns = [
    path('', ActiveGolfProblemList.as_view(), name='home'),
    path('active/', ActiveGolfProblemList.as_view(), name='active'),
    path('past/', PastGolfProblemList.as_view(), name='past'),
    path('future/', FutureGolfProblemList.as_view(), name='future'),
    path('p/<pid>/', problem_detail, name='problem'),
    path('p/<pid>/leaders/', problem_leader_view, name='prob_leader'),

    path('leaders/', user_leader_view, name='user_leader'),
    path('rules/', rules_view, name='rules'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

