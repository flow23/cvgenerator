from django.contrib import admin
from generator.models import *

class TemplateSettingInline(admin.StackedInline):
	model = Template_Setting
	extra = 0

class TemplateAdmin(admin.ModelAdmin):
	fieldsets = [
		('Template', {'fields': ['name', 'description']}),
	]
	inlines = [TemplateSettingInline]
	list_display = ('name', 'description', 'count_settings', 'last_change', 'creation_date')
	search_fields = ['name']
	date_hierarchy = 'last_change'

admin.site.register(Template, TemplateAdmin)
