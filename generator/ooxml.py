from docx  import *

class OOXMLDocument():
	def __init__(self):
		global title
		global subject
		global creator
		global keywords

	def setDocumentInformation(self, title=None, subject=None, creator=None, keywords=None):
		return self


	def presave(self):
		# Create our properties, contenttypes, and other support files
		self.title    = 'Python docx demo'
        self.subject  = 'A practical example of making docx from Python'
        self.creator  = 'Mike MacCana'
        self.keywords = ['python', 'Office Open XML', 'Word']

        coreprops = coreproperties(title=title, subject=subject, creator=creator,
                            keywords=keywords)
        appprops = appproperties()
        contenttypes = contenttypes()
        websettings = websettings()
        wordrelationships = wordrelationships(relationships)

	def save(self, filename):
		presave()

