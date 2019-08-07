from django import forms

from .models import Vote


class VoteForm(forms.ModelForm):
    school = forms.CharField(max_length=1000)
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
            'school', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7',
            'q8', 'qb1', 'qb2', 'qb3', 'qb4',
        ]

    def clean_q1(self, *args, **kwargs):
        q1 = self.cleaned_data.get("q1")
        return cleaner(q1)

    def clean_q2(self, *args, **kwargs):
        q2 = self.cleaned_data.get("q2")
        return cleaner(q2)

    def clean_q3(self, *args, **kwargs):
        q3 = self.cleaned_data.get("q3")
        return cleaner(q3)

    def clean_q4(self, *args, **kwargs):
        q4 = self.cleaned_data.get("q4")
        return cleaner(q4)

    def clean_q5(self, *args, **kwargs):
        q5 = self.cleaned_data.get("q5")
        return cleaner(q5)

    def clean_q6(self, *args, **kwargs):
        q6 = self.cleaned_data.get("q6")
        return cleaner(q6)

    def clean_q7(self, *args, **kwargs):
        q7 = self.cleaned_data.get("q7")
        return cleaner(q7)

    def clean_q8(self, *args, **kwargs):
        q8 = self.cleaned_data.get("q8")
        return cleaner(q8)


def cleaner(q):
    if q < 1 or q > 10:
        raise forms.ValidationError("This is not a number between 1 and 10")
    return q


