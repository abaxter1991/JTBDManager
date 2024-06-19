from django.urls import path, include

from .views import (
    ProjectCreateView,
    ProjectDeleteView,
    ProjectDetailView,
    ProjectListView,
    ProjectUpdateView,
)

app_name = 'projects'

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('<str:project_slug>/', ProjectDetailView.as_view(), name='project-detail'),
    path('<str:project_slug>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('<str:project_slug>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('<str:project_slug>/', include(('jobs.urls', 'jobs'), namespace='jobs')),
]
