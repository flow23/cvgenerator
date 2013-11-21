from django.db.models import Max

from generator.models import Generator

def get_latest_generated_cv_by_user(limit=None):
    a = Generator.objects.values("employee").annotate(latest_id=Max('id'))
    a = list(v['latest_id'] for v in a)
    if limit:
    	return Generator.objects.filter(id__in=a).order_by('-creation_date')[:limit]
    return Generator.objects.filter(id__in=a).order_by('-creation_date')

'''
def get_latest_generated_cv_by_user_desc(limit=None, **filters):
    a = Generator.objects.values("employee").annotate(latest_id=Max('id'))
    a = list(v['latest_id'] for v in a)
    if limit:
    	return Generator.objects.filter(**filters).order_by('-creation_date')[:limit]
    return Generator.objects.filter(**filters).order_by('-creation_date')
'''
