from django import forms
from generator.models import Generator

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

        latex.process_latex('latex/document_xelatex.tex', context={"g" : g}, outtype='pdf', outfile_pdf=str(g.pdf_file), outfile_tex=str(g.tex_file))

        g.status = 'F'

        if commit:
            g.save()

        return g
