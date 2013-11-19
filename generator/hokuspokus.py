import os, time
from django.conf import settings

from docx import *

class Hokuspokus:

    def save(self, filename=None):
        # Save our document
        if filename:
            savedocx(document, coreprops, appprops, contenttypes, websettings,
                wordrelationships, os.path.join(settings.MEDIA_ROOT, str(filename)))
        else:
            timestamp = str(time.time())
            savedocx(document, coreprops, appprops, contenttypes, websettings,
                wordrelationships, os.path.join(settings.MEDIA_ROOT, timestamp + '.docx'))

    def __init__(self, template=None):
        global document
        global coreprops
        global appprops
        global contenttypes
        global websettings
        global wordrelationships

        # Default set of relationshipships - the minimum components of a document
        relationships = relationshiplist()

        # Make a new document tree - this is the main part of a Word document
        document = newdocument()

        # This xpath location is where most interesting content lives
        body = document.xpath('/w:document/w:body', namespaces=nsprefixes)[0]

        # Append a table
        tbl_rows = [ ['A1', 'A2']
                   , ['B1', 'B2']
                   , ['C1', 'C2']
                   ]
        tblw = 50*95
        twunit = 'pct'
        body.append(table(tbl_rows, tblw = tblw, twunit = twunit))

        # Add a pagebreak
        body.append(pagebreak(type='page', orient='portrait'))

        body.append(heading('Ideas? Questions? Want to contribute?', 2))
        body.append(paragraph('Email <python.docx@librelist.com>'))

        # Create our properties, contenttypes, and other support files
        title    = 'Python docx demo'
        subject  = 'A practical example of making docx from Python'
        creator  = 'Mike MacCana'
        keywords = ['python', 'Office Open XML', 'Word']

        coreprops = coreproperties(title=title, subject=subject, creator=creator,
                            keywords=keywords)
        appprops = appproperties()
        contenttypes = contenttypes()
        websettings = websettings()
        wordrelationships = wordrelationships(relationships)
