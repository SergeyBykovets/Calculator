from django.shortcuts import render
from django import forms

class PSUForm(forms.Form):
    CPU = [
        ('', '--- Оберіть процесор ---'),
    ]

    GPU= [
        ('', '--- Оберіть відеокарту ---'),
    ]

    cpu = forms.ChoiceField(choices=CPU, label="Процесор", required=True)
    gpu = forms.ChoiceField(choices=GPU, label="Відеокарта", required=True)


def main(request):
    form = PSUForm()
    return render(request, 'main/main.html', {"form": form})


