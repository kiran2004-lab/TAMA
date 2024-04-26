# teammatesmodule/views.py
from .models import PersonalTaskDetails
from django.shortcuts import render,redirect, get_object_or_404
from teamleadmodule.models import TaskDetails

def viewtasks(request):
    return render(request, 'teammatesmodule/viewtasks.html')


def personaltaskpost(request):
    return render(request, 'teammatesmodule/personaltaskpost.html')


def view_personal_task_details(request):
    personal_task_details_list = PersonalTaskDetails.objects.all()
    return render(request, 'teammatesmodule/view_personal_task_details.html', {'personal_task_details_list': personal_task_details_list})


def add_personal_task_details(request):
    if request.method == 'POST':
        Task_Title = request.POST.get('TaskTitle')
        Task_Priority = request.POST.get('TaskPriority')
        Start_Date = request.POST.get('StartDate')
        End_Date = request.POST.get('EndDate')
        Description = request.POST.get('Description')
        Task_Details = PersonalTaskDetails(
            Task_Title=Task_Title,
            Task_Priority=Task_Priority,
            Start_Date=Start_Date,
            End_Date=End_Date,
            Description=Description,
        )
        Task_Details.save()
        return render(request, 'teammatesmodule/datainsertion.html')
    return render(request, 'teammatesmodule/teammateshomepage.html')


def task_details_list(request):
    task_details_list = TaskDetails.objects.all()
    return render(request, 'teammatesmodule/viewtasks.html',{'task_details_list':task_details_list})

def edit_personal_task_details(request, task_id):
    task_details = get_object_or_404(PersonalTaskDetails, id=task_id)
    if request.method == 'POST':
        task_details.Task_Title = request.POST.get('TaskTitle')
        task_details.Task_Priority = request.POST.get('TaskPriority')
        task_details.Start_Date = request.POST.get('StartDate')
        task_details.End_Date = request.POST.get('EndDate')
        task_details.Description = request.POST.get('Description')
        task_details.save()
        return redirect('teammatesmodule:view_personal_task_details')
    return render(request, 'teammatesmodule/edit_personal_task_details.html', {'task_details': task_details})

def delete_personal_task_details(request, task_id):
    task_details = get_object_or_404(PersonalTaskDetails, id=task_id)
    if request.method == 'POST':
        task_details.delete()
        return redirect('teammatesmodule:view_personal_task_details')
    return render(request, 'teammatesmodule/delete_personal_task_details.html', {'task_details': task_details})