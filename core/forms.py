from django import forms

from core.models import STANDARD_CHAR_SIZE, ToDo, CHOICES


class ToDoForm(forms.ModelForm):
    title = forms.CharField(
        max_length=STANDARD_CHAR_SIZE,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'name': 'title',
            'placeholder': 'e.g.- Buy Veggies'
        })
    )
    priority_code = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': "form-control", 'name': "priority_code",
                   'id': "floatingSelect", 'aria-label': "Floating label select example"}
        ), choices=CHOICES
    )

    class Meta:
        model = ToDo
        exclude = ('for_date', 'created_at', 'updated_at', 'is_completed')
