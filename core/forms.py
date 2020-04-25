from django import forms


class ScrapeForm(forms.Form):
    hidden = forms.HiddenInput()
