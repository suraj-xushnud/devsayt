from django.db.models import Q
from django.views.generic import ListView
from django.contrib.auth import get_user_model


User = get_user_model()


class DevelopersView(ListView):
    template_name = 'app_main/developers.html'
    queryset = User.objects.exclude(
        Q(bio=None) | Q(occupation=None) | Q(location=None) |
        Q(bio='') | Q(occupation='') | Q(location='')
    )
    context_object_name = 'developers'