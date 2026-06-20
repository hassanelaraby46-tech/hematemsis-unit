from django import forms
from .models import GaharChecklist

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = GaharChecklist
        fields = ['department', 'patient_id_verified', 'policies_updated', 
                  'hand_hygiene_followed', 'waste_segregation_correct', 'notes']
        widgets = {
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
            'patient_id_verified': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'policies_updated': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'hand_hygiene_followed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'waste_segregation_correct': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      }