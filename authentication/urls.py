from django.urls import path
from . import views
# from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'authentication'


urlpatterns = [
  path('login/', views.login),

  # path('events/<int:id>', views.events_detail),

  # path('questions/', views.questions_list),

  # path('questions/<int:id>', views.questions_detail),

  # path('getQuestionsByEventCode/', views.questions_by_eventId),
]


# urlpatterns = format_suffix_patterns(urlpatterns)