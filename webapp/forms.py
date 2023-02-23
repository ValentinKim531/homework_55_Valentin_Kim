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
            raise ValidationError("Заголоаок должен быть длиннее 2 символов")
        return title
