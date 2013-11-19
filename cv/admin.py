from django.contrib import admin
from cv.models import *

'''
from django.contrib import admin
from movie.models import Movie, Rating

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1


class RatingAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None,     {'fields': ['rating']}),
                 ('Date information', {'fields': ['publication_date'], 'classes': ['collapse']}),
                 ]
    list_display = ('rating', 'movie', 'publication_date','was_published_recently')

admin.site.register(Rating, RatingAdmin)

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
                 ('Movie information', {'fields': ['imdb_id','imdb_title','imdb_year','imdb_cover_url']}),
                 ('Date information', {'fields': ['publication_date'], 'classes': ['collapse']}),
                 ]
    inlines = [RatingInline]
    list_display = ('imdb_id','imdb_title','imdb_year','publication_date','average_rating','number_of_ratings','was_published_recently')
    list_filter = ['publication_date']
    search_fields = ['imdb_title']
    date_hierarchy = 'publication_date'

admin.site.register(Movie, MovieAdmin)
'''

class SkillInline(admin.StackedInline):
	model = Skill
	extra = 0

class ProjectInline(admin.StackedInline):
	model = Project
	extra = 0

class TrainingInline(admin.StackedInline):
	model = Training
	extra = 0

class EducationInline(admin.StackedInline):
	model = Education
	extra = 0

class SpokenLanguageInline(admin.StackedInline):
	model = Spoken_Language
	extra = 0

class EmployeeAdmin(admin.ModelAdmin):
	fieldsets = [
		('Mitarbeiter', {'fields': [('first_name', 'last_name'), 'position']}),
		('Beschreibung', {'fields': ['short_description'], 'classes': ['']}),
		('Zusatzinformationen', {'fields': ['place_of_birth', 'year_of_birth', 'family_status', 'citizenship'], 'classes': ['collapse']}),
	]
	inlines = [SkillInline, ProjectInline, TrainingInline, EducationInline, SpokenLanguageInline]
	list_display = ('first_name', 'last_name', 'position', 'count_skills', 'count_projects', 'last_change', 'creation_date')
	search_fields = ['first_name', 'last_name']
	date_hierarchy = 'last_change'

admin.site.register(Employee, EmployeeAdmin)

class CustomerAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name']}),
	]

admin.site.register(Customer, CustomerAdmin)