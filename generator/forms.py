from django import forms
from generator.models import Generator
from cv import services

import latex

class GeneratorForm(forms.ModelForm):
    class Meta:
        model = Generator
        exclude = ('status','pdf_file','tex_file')

    def save(self, commit=True, force_insert=False, force_update=False, *args, **kwargs):
        g = super(GeneratorForm, self).save(commit=False, *args, **kwargs)

        if commit:
            g.save()

        # Overriding empty filename from form before saving to db
        g.pdf_file = g.generate_filename(g.id, g.employee, g.template, 'pdf')
        g.tex_file = g.generate_filename(g.id, g.employee, g.template, 'tex')

        if commit:
            g.save()

        skill_list = services.get_skills_by_employee_id(g.employee.id)
        project_list = services.get_projects_by_employee_id(g.employee.id)
        education_list = services.get_educations_by_employee_id(g.employee.id)
        training_list = services.get_trainings_by_employee_id(g.employee.id)
        spoken_languages_list = services.get_spoken_languages_by_employee_id(g.employee.id)

        latex_context={'g' : g,
        'skill_list' : skill_list,
        'project_list' : project_list,
        'education_list' : education_list,
        'training_list' : training_list,
        'spoken_languages_list' : spoken_languages_list}
        latex.process_latex(g.template.tex_file, context=latex_context, outtype='pdf', outfile_pdf=str(g.pdf_file), outfile_tex=str(g.tex_file))

        g.status = 'F'

        if commit:
            g.save()

        return g
