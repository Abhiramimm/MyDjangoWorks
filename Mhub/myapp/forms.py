from django import forms

class MovieForm(forms.Form):

    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-danger"}))

    year=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-danger"}))

    director=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-danger"}))

    run_time=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control border border-danger"}))

    language=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-danger"}))

    genre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-danger"}))

    producer=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-danger"}))