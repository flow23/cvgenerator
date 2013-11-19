from django.views import generic

from generator.services import get_latest_generated_cv_by_user
from generator.template_normal import Hokuspokus

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_cv_by_employee'
    #Hokuspokus().save('abcd')

    def get_queryset(self):
        #queryset = get_latest_generated_cv_by_user
        #return queryset

        return get_latest_generated_cv_by_user()
