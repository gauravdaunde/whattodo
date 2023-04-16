from core.models import ToDo


def get_todos():
    return ToDo.objects.all().order_by('priority_code')
