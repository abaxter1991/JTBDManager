from django.urls import path

from .views import (
    JobListView,
    JobDetailView,
    AcceptanceCriteriaListView,
    AcceptanceCriteriaDetailView,
)

app_name = 'jobs'

urlpatterns = [
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('<str:job_slug>/', JobDetailView.as_view(), name='job-detail'),
    path(
        '<str:job_slug>/acceptance_criteria/',
        AcceptanceCriteriaListView.as_view(),
        name='acceptance-criteria-list',
    ),
    path(
        '<str:job_slug>/<str:acceptance_criteria_id>/',
        AcceptanceCriteriaDetailView.as_view(),
        name='acceptance-criteria-detail',
    ),
]
