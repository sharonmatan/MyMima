from django import forms


class SearchString(forms.Form):
    search_results = forms.CharField(max_length=300)