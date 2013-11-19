from django import forms
from generator.models import Generator

from generator.hokuspokus import Hokuspokus

class GeneratorForm(forms.ModelForm):
    class Meta:
        model = Generator
        exclude = ('status','cv_file',)

    def generate_cv(self, filename=None):
        Hokuspokus().save(filename)
        pass

    def save(self, commit=True, force_insert=False, force_update=False, *args, **kwargs):
        m = super(GeneratorForm, self).save(commit=False, *args, **kwargs)

        if commit:
            m.save()

        # Overriding empty filename from form before saving to db
        m.cv_file = m.generate_filename(m.id, m.employee, m.template)

        if commit:
            m.save()

        Hokuspokus().save(m.cv_file)
        #self.generate_cv(m.cv_file)

        m.status = 'F'

        if commit:
            m.save()

        return m
