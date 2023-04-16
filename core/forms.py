from django import forms

from core.models import STANDARD_CHAR_SIZE, ToDo


class ToDoForm(forms.ModelForm):
    title = forms.CharField(max_length=STANDARD_CHAR_SIZE)
    priority_code = forms.IntegerField()

    class Meta:
        model = ToDo
        exclude = ('for_date', 'created_at', 'updated_at', 'is_completed')
