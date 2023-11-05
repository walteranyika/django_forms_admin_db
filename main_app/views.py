from django.shortcuts import render, redirect

# Create your views here.
from main_app.app_forms import StudentForm, EmployeeForm, UploadImagesForm
from main_app.models import Student, UploadImages


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


def employee_add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            for error in form.errors:
                print(error)
    else:
        form = EmployeeForm()
    return render(request, "employee/index.html", {"form": form})


def employees_view(request):
    return None


def students_view(request):
    return None


def upload_images(request):
    if request.method == 'POST':
        form = UploadImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_object = form.instance
            return render(request, 'testing.html', {'form': form, 'img_obj': img_object})
    else:
        form = UploadImagesForm()
    return render(request, "testing.html", {"form": form})
