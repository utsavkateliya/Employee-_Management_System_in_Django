from django.shortcuts import get_object_or_404, render , redirect, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.contrib import messages

# Create your views here.

def index(request):
    emps = Employee.objects.all()
    context = {
         'emps' : emps
    }
    return render(request, 'index.html', context)

def update_emp(request, emp_id):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        phone = request.POST.get('phone')
        edit = Employee.objects.get(id=emp_id)
        edit.first_name=first_name
        edit.last_name=last_name
        edit.salary=salary
        edit.bonus=bonus
        edit.dept= Department.objects.get(name=dept)
        edit.role= Role.objects.get(name=role)
        edit.phone=phone
        edit.save()
        messages.success(request,"Employee Data Updated")
        return redirect("/")
    
    emp = Employee.objects.get(id=emp_id)
    context = {'emp':emp}
    return render(request,"update.html",context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        dept = request.POST['dept']
        role = request.POST['role']
        phone = request.POST['phone']
        hire_date = request.POST['hire_date']
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, dept=Department.objects.get(name=dept), role=Role.objects.get(name=role), phone=phone, hire_date=datetime.now())
        new_emp.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")
    return render(request, 'add.html')

def delete_emp(request,emp_id):
    emps = get_object_or_404(Employee, id=emp_id)
    emps.delete()
    messages.success(request,"Employee Data Deleted Successfully")
    return redirect("/")
   

    
def view_emp(request):
    emps = Employee.objects.all()
    context = {
            'emps' : emps
        }
    # print(context) # to check if the value is getting printed from the database or not 
    return render(request, 'view.html', context)