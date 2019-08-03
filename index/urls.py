from django.urls import path
from .views import index, results, vote, detail

app_name = 'polls'

urlpatterns = [
    path('', index, name='main'),
    path('<int:question_id>}', detail, name='detail'),
    path('<int:question_id>/results', results, name='results'),
    path('<int:question_id>/vote', vote, name='vote')
]
