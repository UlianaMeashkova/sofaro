from django import forms
from products.models import Comment, Score

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
    age = forms.IntegerField(min_value=18, required=False)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )

class BookingForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ("value",)

    def __init__(self, *args, **kwargs):
        super(ScoreForm, self).__init__(*args, **kwargs)

        self.fields['value'].widget.attrs.update({"min": 1, "max": 5})
