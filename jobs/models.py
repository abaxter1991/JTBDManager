from django.db import models

from accounts.models import Account
from projects.models import Project
from common.models import CommonModel, CommonSlugModel
from .managers import JobManager

# These status choices are being used in all models in this file.
# TODO: Manage these choices better by creating a StatusChoices class that inherits models.TextChoices
#       https://docs.djangoproject.com/en/3.2/ref/models/fields/#enumeration-types
BACKLOG = 'Backlog'
TO_BE_DONE = 'ToBeDone'
IN_PROGRESS = 'InProgress'
IN_REVIEW = 'InReview'
IN_TESTING = 'InTesting'
CANCELED = 'Canceled'
COMPLETED = 'Completed'
STATUS_CHOICES = (
    (BACKLOG, 'Backlog'),
    (TO_BE_DONE, 'To Be Done'),
    (IN_PROGRESS, 'In Progress'),
    (IN_REVIEW, 'In Review'),
    (IN_TESTING, 'In Testing'),
    (CANCELED, 'Canceled'),
    (COMPLETED, 'Completed'),
)


class Job(CommonSlugModel):
    title = models.CharField(max_length=100, unique=True, verbose_name='Title')
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Project')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=BACKLOG, verbose_name='Status')

    objects = JobManager()

    class Meta:
        db_table = 'job'

    def __str__(self):
        return self.title


class Story(CommonModel):
    SUPPORT_AGENT = 'SupportAgent'
    PROPERTY_MANAGER = 'PropertyManager'
    CLIENT = 'Client'
    DEVELOPER = 'Developer'
    MAIN_CHARACTER_CHOICES = (
        (SUPPORT_AGENT, 'Support Agent'),
        (PROPERTY_MANAGER, 'Property Manager'),
        (CLIENT, 'Client'),
        (DEVELOPER, 'Developer'),
    )

    job = models.ForeignKey(Job, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Job')
    title = models.CharField(max_length=100, unique=True, verbose_name='Title')
    author = models.ForeignKey(Account, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Author')
    main_character = models.CharField(
        max_length=50,
        choices=MAIN_CHARACTER_CHOICES,
        default=SUPPORT_AGENT,
        verbose_name='Main Character',
    )
    story = models.TextField(verbose_name='Story')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=BACKLOG, verbose_name='Status')

    class Meta:
        db_table = 'story'
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    def __str__(self):
        return self.title


class AcceptanceCriteria(CommonModel):
    CHAPTER = 'Chapter'
    SECTION = 'Section'
    SUBSECTION = 'Subsection'
    SECTION_TYPE_CHOICES = (
        (CHAPTER, 'Chapter'),
        (SECTION, 'Section'),
        (SUBSECTION, 'Subsection'),
    )

    job = models.ForeignKey(Job, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Job')
    title = models.CharField(max_length=100, unique=True, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=BACKLOG, verbose_name='Status')
    section_type = models.CharField(max_length=50, choices=SECTION_TYPE_CHOICES, verbose_name='Section Type')
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='parent_reference',
        verbose_name='Parent',
    )
    sibling = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='sibling_reference',
        verbose_name='Sibling',
    )
    # TODO: Remove the Jira ticket fields and create an integrations app that contains models
    #       for Jira data that will contain relationships to other models in the jobs app
    jira_design_tickets = models.CharField(max_length=100, unique=True, verbose_name='Jira Design Tickets')
    jira_developer_tickets = models.CharField(max_length=100, unique=True, verbose_name='Jira Developer Tickets')
    jira_test_tickets = models.CharField(max_length=100, unique=True, verbose_name='Jira Test Tickets')

    class Meta:
        db_table = 'acceptance_criteria'
        verbose_name = 'Acceptance Criteria'
        verbose_name_plural = 'Acceptance Criteria'

    def __str__(self):
        return self.title
