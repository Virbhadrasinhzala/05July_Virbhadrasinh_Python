from django import forms
from .models import p_signup,contact_us,book_apointment

class psignup(forms.ModelForm):
    class Meta:
        model=p_signup
        fields='__all__'


class a_book(forms.ModelForm):
    class Meta:
        model=book_apointment
        fields='__all__'


class contactus(forms.ModelForm):
    class Meta:
        model=contact_us
        fields='__all__'