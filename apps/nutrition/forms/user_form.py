from django import forms
from ..models.user import SimpleUser

class SimpleUserForm(forms.ModelForm):
    class Meta:
        model = SimpleUser
        fields = ['first_name', 'last_name', 'student_number', 'strategy_type']
