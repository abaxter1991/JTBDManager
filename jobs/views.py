from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from projects.models import Project
from .models import Job, Story, AcceptanceCriteria


class JobListView(LoginRequiredMixin, ListView):
    template_name = 'jobs/job-list.html'
    context_object_name = 'job_list'
    model = Job

    def get_queryset(self):
        project_slug = self.kwargs.get('project_slug')
        project_obj = Project.objects.get(slug=project_slug)
        queryset = Job.objects.filter(project_id=project_obj.id)
        search_query = self.request.GET.get('search')

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        project_slug = self.kwargs.get('project_slug')

        context = super(JobListView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(slug=project_slug)

        return context


class JobCreateView(LoginRequiredMixin, CreateView):
    pass


class JobDetailView(LoginRequiredMixin, DetailView):
    template_name = 'jobs/job-detail.html'
    context_object_name = 'job'
    model = Job

    def get_object(self, *args, **kwargs):
        job_slug = self.kwargs.get('job_slug')

        return Job.objects.get(slug=job_slug)

    def get_context_data(self, **kwargs):
        project_slug = self.kwargs.get('project_slug')

        context = super(JobDetailView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(slug=project_slug)

        return context


class JobUpdateView(LoginRequiredMixin, UpdateView):
    pass


class JobDeleteView(LoginRequiredMixin, DeleteView):
    pass


class StoryListView(LoginRequiredMixin, ListView):
    pass


class StoryCreateView(LoginRequiredMixin, CreateView):
    pass


class StoryDetailView(LoginRequiredMixin, DetailView):
    pass


class StoryUpdateView(LoginRequiredMixin, UpdateView):
    pass


class StoryDeleteView(LoginRequiredMixin, DeleteView):
    pass


class AcceptanceCriteriaListView(LoginRequiredMixin, ListView):
    template_name = 'jobs/acceptance-criteria-list.html'
    context_object_name = 'acceptance_criteria_list'
    model = AcceptanceCriteria

    def get_queryset(self):
        job_slug = self.kwargs.get('job_slug')
        job_obj = Job.objects.get(slug=job_slug)
        queryset = AcceptanceCriteria.objects.filter(job_id=job_obj.id)
        search_query = self.request.GET.get('search')

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        project_slug = self.kwargs.get('project_slug')
        job_slug = self.kwargs.get('job_slug')

        context = super(AcceptanceCriteriaListView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(slug=project_slug)
        context['job'] = Job.objects.get(slug=job_slug)

        return context


class AcceptanceCriteriaCreateView(LoginRequiredMixin, CreateView):
    pass


class AcceptanceCriteriaDetailView(LoginRequiredMixin, DetailView):
    template_name = 'jobs/acceptance-criteria-detail.html'
    context_object_name = 'acceptance_criteria'
    model = Job

    def get_object(self, *args, **kwargs):
        acceptance_criteria_id = self.kwargs.get('acceptance_criteria')

        return AcceptanceCriteria.objects.get(id=acceptance_criteria_id)

    def get_context_data(self, **kwargs):
        job_slug = self.kwargs.get('job_slug')

        context = super(AcceptanceCriteriaDetailView, self).get_context_data(**kwargs)
        context['acceptance_criteria'] = AcceptanceCriteria.objects.get(slug=job_slug)

        return context


class AcceptanceCriteriaUpdateView(LoginRequiredMixin, UpdateView):
    pass


class AcceptanceCriteriaDeleteView(LoginRequiredMixin, DeleteView):
    pass
