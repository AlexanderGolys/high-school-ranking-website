from django import forms

from .models import Vote


class VoteForm(forms.ModelForm):
    q1 = forms.IntegerField()
    q2 = forms.IntegerField()
    q3 = forms.IntegerField()
    q4 = forms.IntegerField()
    q5 = forms.IntegerField()
    q6 = forms.IntegerField()
    q7 = forms.IntegerField()
    q8 = forms.IntegerField()
    qb1 = forms.BooleanField(required=False, initial=False)
    qb2 = forms.BooleanField(required=False, initial=False)
    qb3 = forms.BooleanField(required=False, initial=False)
    qb4 = forms.BooleanField(required=False, initial=False)
    more_info = forms.CharField(required=False, max_length=1000)

    class Meta:
        model = Vote
        fields = [
            'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7',
            'q8', 'qb1', 'qb2', 'qb3', 'qb4',
        ]