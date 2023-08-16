from .models import Customer
from django import forms
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def validate_mobile_num(self):
        mobile = self.cleaned_data.get('mobile_number')
        if mobile < 10:
            raise forms.ValidationError('you must enter at least 10 numbers')
        return mobile