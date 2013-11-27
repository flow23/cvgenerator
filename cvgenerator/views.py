from django.views import generic

from generator.services import get_latest_generated_cv_by_user

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_cv_by_employee'

    def get_queryset(self):
        return get_latest_generated_cv_by_user()
