from django import forms
from products.models import Comment

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
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
    age = forms.IntegerField(min_value=18, required=False)

# class CommentForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['author'].disabled = True


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')