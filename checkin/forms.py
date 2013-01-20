from django import forms
from django.contrib.auth.models import User
from models import CheckIn, CheckOut

class CheckInOutForm(forms.Form):
    username = forms.CharField()
    isCheckIn = forms.BooleanField(initial=True, required=False)

    def clean(self):
        cleaned_data = super(CheckInOutForm, self).clean()
        user, created = User.objects.get_or_create(username=cleaned_data['username'])
        if created:
            user.is_active = False
        user.save()
        cleaned_data["user"] = user


        print cleaned_data["isCheckIn"]
        if cleaned_data["isCheckIn"]:
            lastCheckIn = CheckIn.objects.filter(climber=user, checkOut=None)
            if lastCheckIn:
                raise forms.ValidationError("%s is already checked in" % user.username)
        else:
            lastCheckIn = CheckIn.objects.filter(climber=user, checkOut=None)
            if not lastCheckIn:
                raise forms.ValidationError("%s is already checked out" % user.username)

        return cleaned_data