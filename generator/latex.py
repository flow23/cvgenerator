import subprocess 
from subprocess import call, PIPE, CalledProcessError
import os
import tempfile

from django.template import loader, Context, TemplateDoesNotExist
from django.conf import settings
from django.http import Http404

def process_latex(template, context=None, outtype='pdf', outfile_pdf=None, outfile_tex=None):
    """
    Processes a template as a LaTeX source file.
    Output is either being returned or stored in outfile.
    At the moment only pdf output is supported.
    """
    try:
        if type(template) in (list, tuple):
            t = loader.select_template(template)
        else:
            t = loader.get_template(template)
        c = Context(context)
        r = t.render(c)
        r = r.encode("utf-8")
        fd,base = tempfile.mkstemp()
        tex = os.fdopen(fd, "w")
        tex.write(r)
        #tex.flush()
        #base = tex.name
        #print "base:",base
        tex.close()
        items = "log aux pdf dvi png".split()
        names = dict((x, '%s.%s' % (base, x)) for x in items)
        output = names[outtype]

        if outtype == 'pdf' or outtype == 'dvi':
            #pdflatex(base, outtype)
            xelatex(base, outtype)
        elif outtype == 'png':
            pdflatex(base, 'dvi')
            call(['dvipng', '-bg', '-transparent',
                  names['dvi'], '-o', names['png']],
                  cwd=os.path.dirname(base), 
                  stdout=PIPE, stderr=PIPE)

        os.remove(names['log'])
        os.remove(names['aux'])

        if outfile_tex:
            os.rename(base, os.path.join(settings.MEDIA_ROOT, outfile_tex))
        else:
            os.remove(base)

        if not outfile_pdf:
            o = file(output).read()
            os.remove(output)
            return o
        else:
            os.rename(output, os.path.join(settings.MEDIA_ROOT, outfile_pdf))
    except OSError:
        raise Http404("500 - Internal Server Error.\nError generating CV.")
    #except TemplateDoesNotExist:
        #raise Http404("500 - Internal Server Error.\nTemplate does not exist.")
    except CalledProcessError:
        raise Http404("500 - Internal Server Error.\nLatex engine failed.")

def pdflatex(outfile, outtype='pdf'):
    """
    Calls pdflatex on command line with predefined parameters
    """
    dirname,filename = os.path.split(outfile)
    
    #print "dirname:", dirname
    #print "filename:", filename
    
    subprocess.check_call(
      ['pdflatex', '-interaction=nonstopmode',
                            '-output-format', outtype, 
                            filename],
               cwd=dirname) #, stdout=PIPE, stderr=PIPE)

def xelatex(outfile, outtype='pdf'):
    """
    Calls xelatex on command line with predefined parameters
    """
    dirname,filename = os.path.split(outfile)
    subprocess.check_call(
      ['xelatex', '-interaction=nonstopmode', filename],
               cwd=dirname) #, stdout=PIPE, stderr=PIPE)