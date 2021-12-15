from allauth.account.forms import SignupForm
from django import forms


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, label="姓")
    last_name = forms.CharField(max_length=30, label="名")
    department = forms.CharField(max_length=30, label="所属", required=False)
    # created = forms.CharField(max_length=30, label="")


class SignupUserForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="姓")
    last_name = forms.CharField(max_length=30, label="名")

    def save(self, request):
        """
        サインアップボタンがクリックされた時の処理

        Args:
            request ([type]): [description]
        """
        user = super(SignupUserForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user
