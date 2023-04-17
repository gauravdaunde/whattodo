import datetime

from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from core.business import get_todos
from core.forms import ToDoForm
from core.models import ToDo


class IndexPage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        form = ToDoForm()
        context = {
            'todos': get_todos(),
            'form': form
        }
        return context


class CreateToDoCreateView(TemplateView):
    template_name = 'home.html'

    def post(self, request):
        # create a form instance and populate it with data from the request:
        form = ToDoForm(request.POST)
        # check whether it's valid:
        context = {'form': form}
        if form.is_valid():
            todo = form.save(commit=False)
            todo.name = None
            todo.for_date = datetime.datetime.now()
            try:
                todo.save()
            except IntegrityError as e:
                form.add_error('title', 'ToDo with given title and priority already exists')
            if not form.errors:
                return HttpResponseRedirect('/')

        return render(request, self.template_name, context=context)


class ToDoDeleteView(TemplateView):
    template_name = 'home.html'

    def get(self, request, todo_id, *args, **kwargs):
        ToDo.objects.filter(id=todo_id).delete()
        return HttpResponseRedirect('/')
