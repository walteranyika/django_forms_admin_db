from django.shortcuts import render, redirect

# Create your views here.
from main_app.app_forms import StudentForm
from main_app.models import Student


def students(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            dob = form.cleaned_data['dob']
            phone = form.cleaned_data['phone']
            gender = form.cleaned_data['gender']
            is_completed = form.cleaned_data['is_completed']
            data = form.cleaned_data
            print(type(data))
            print("All Data has been cleaned")
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                dob=dob,
                gender=gender,
                is_completed=is_completed)
            return redirect(to="/")
    context = {"form": StudentForm()}
    return render(request, "index.html", context)
