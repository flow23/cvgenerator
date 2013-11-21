from cv.models import Skill, Project, Spoken_Language, Training, Education

def get_skills_by_employee_id(employee_id):
    s = Skill.objects.filter(employee__id=employee_id)

    return s

def get_projects_by_employee_id(employee_id):
	p = Project.objects.filter(employee__id=employee_id).order_by('-work_end')

	return p

def get_spoken_languages_by_employee_id(employee_id):
	sl = Spoken_Language.objects.filter(employee__id=employee_id)

	return sl

def get_trainings_by_employee_id(employee_id):
	t = Training.objects.filter(employee__id=employee_id).order_by('description')

	return t

def get_educations_by_employee_id(employee_id):
	e = Education.objects.filter(employee__id=employee_id)

	return e
