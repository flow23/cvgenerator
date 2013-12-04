from django.views import generic

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from generator.models import Generator
from generator.forms import GeneratorForm

class GeneratorIndexView(generic.ListView):
    template_name = 'generator/index.html'
    context_object_name = 'generator_list'

    def get_queryset(self):
        return Generator.objects.order_by('-creation_date')[:25]

class GeneratorCreateView(generic.CreateView):
    form_class = GeneratorForm
    model = Generator
    fields = ['employee', 'template']
    template_name = 'generator/generator_create_form.html'

    def form_valid(self, form):
        #form.generate_cv()
        form.instance.created_by = self.request.user
        return super(GeneratorCreateView, self).form_valid(form)

    #@method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GeneratorCreateView, self).dispatch(*args, **kwargs)

class GeneratorDetailView(generic.DetailView):
    model = Generator
    template_name = 'generator/detail.html'

    ''' Aendern von Daten beim Aufrufen der View
        def get_object(self):
        # Call the superclass
        object = super(AuthorDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object
    '''
