from django import forms

class QuestionForm(forms.Form):
  image = forms.CharField(widget=forms.HiddenInput)

  recognizability = forms.TypedChoiceField(choices=((str(x), x) for x in range(1, 6)), coerce=int, widget=forms.RadioSelect)
  familiarity = forms.TypedChoiceField(choices=((str(x), x) for x in range(1, 6)), coerce=int, widget=forms.RadioSelect)
  pleasantness = forms.TypedChoiceField(choices=((str(x), x) for x in range(1, 6)), coerce=int, widget=forms.RadioSelect)
  complexity = forms.TypedChoiceField(choices=((str(x), x) for x in range(1, 6)), coerce=int, widget=forms.RadioSelect)
  memorability = forms.TypedChoiceField(choices=((str(x), x) for x in range(1, 6)), coerce=int, widget=forms.RadioSelect)

  name = forms.CharField(max_length=50)