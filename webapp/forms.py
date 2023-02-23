from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import StatusChoice, To_do


class TodoForm(forms.ModelForm):
    title = forms.CharField(max_length=100, label="Заголовок")
    description = forms.CharField(
        max_length=200, required=True, label="Описание"
    )
    text = forms.CharField(
        max_length=3000,
        required=False,
        label="Текстовое поле",
        widget=widgets.Textarea,
    )
    status = forms.ChoiceField(label="Статус", choices=StatusChoice.choices)
    execution_date = forms.CharField(
        max_length=10, required=False, label="Дата исполнения"
    )

    class Meta:
        model = To_do
        fields = ("title", "description", "text", "status", "execution_date")

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 2:
            raise ValidationError("Title must be longer than 2 characters")
        return title

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) < 2:
            raise ValidationError("Description must be longer than 2 characters")
        return description

    def clean_execution_date(self):
        execution_date = self.cleaned_data.get("execution_date")
        if 0 < len(execution_date) < 10:
            raise ValidationError("Enter the date in the format yyyy.mm.dd or leave the field blank")
        return execution_date
