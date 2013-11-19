#from django.shortcuts import render, get_object_or_404
from django.views import generic

from cv.models import Employee

class IndexView(generic.ListView):
    template_name = 'employee/index.html'
    context_object_name = 'employee_list'

    def get_queryset(self):
        return Employee.objects.order_by('-last_change')[:25]

class DetailView(generic.DetailView):
    model = Employee
    template_name = 'employee/detail.html'

class Generate_FormView(generic.DetailView):
    model = Employee
    template_name = 'employee/generate_form.html'

class UpdateView(generic.UpdateView):
    model = Employee
    fields = ['first_name']
    template_name = 'employee/employee_update_form.html'
    #template_name_suffix = '_update_form'
