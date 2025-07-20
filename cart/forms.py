from django import forms
from accounts.models import User

class usercheckout(forms.ModelForm):
    countery = forms.CharField()
    city = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email','phone','address','postcode','city','country']

    