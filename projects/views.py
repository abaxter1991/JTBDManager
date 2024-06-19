from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .forms import ProjectCreateModelForm
from .models import Project


class ProjectListView(LoginRequiredMixin, ListView):
    template_name = 'projects/project-list.html'
    context_object_name = 'project_list'
    model = Project

    def get_queryset(self):
        queryset = Project.objects.all()
        search_query = self.request.GET.get('search')

        if search_query:
            queryset = Project.objects.filter(title__icontains=search_query)

        return queryset


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'projects/project-create.html'
    form_class = ProjectCreateModelForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projects:project-list')


class ProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = 'projects/project-detail.html'
    context_object_name = 'project'
    model = Project

    def get_object(self, *args, **kwargs):
        project_slug = self.kwargs.get('project_slug')

        return Project.objects.get(slug=project_slug)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'projects/project-create.html'
    form_class = ProjectCreateModelForm

    def get_object(self):
        project_slug = self.kwargs.get('project_slug')

        return Project.objects.get(slug=project_slug)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projects:project-list')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'projects/project-delete.html'

    def get_object(self):
        project_slug = self.kwargs.get('project_slug')

        return Project.objects.filter(slug=project_slug)

    def get_success_url(self):
        return reverse('projects:project-list')
