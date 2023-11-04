from django import forms

CHOICES = (("Male", "Male"), ("Female", "Female"))


class StudentForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50)
    last_name = forms.CharField(label="First Name", max_length=50)
    email = forms.EmailField(label="Email Address")
    phone = forms.CharField(label="Phone Number", max_length=20)
    dob = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
    gender = forms.ChoiceField(choices=CHOICES)
    is_completed = forms.BooleanField(label="Completed?", required=False)
