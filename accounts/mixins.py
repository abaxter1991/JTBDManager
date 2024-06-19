from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class OrganizerAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an organizer."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizer:
            return redirect("user:user-list")

        return super().dispatch(request, *args, **kwargs)


class HomePageLoginRedirectMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("accounts:login")

        return super().dispatch(request, *args, **kwargs)
