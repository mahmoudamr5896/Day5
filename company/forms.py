from django import forms

from .models import TeamLeader ,Epmloyee

class Epm_form(forms.Form):
    name= forms.CharField(max_length=50)
    title= forms.CharField(max_length=50)
    salary=forms.IntegerField()
    team=forms.ChoiceField(choices=[(team.pk,team.pk) for team in TeamLeader.objects.all()],required=True)



class Team_form(forms.Form):
    name= forms.CharField(max_length=50)
    manager=forms.ChoiceField(choices=[(t.name,t.name) for t in Epmloyee.objects.all()],required=True)
