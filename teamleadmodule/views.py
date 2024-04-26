from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskDetails

def taskpost(request):
    return render(request, 'teamleadmodule/taskpost.html')

def add_task_details(request):
    if request.method == 'POST':
        Task_Title = request.POST.get('TaskTitle')
        Task_Priority = request.POST.get('TaskPriority')
        Start_Date = request.POST.get('StartDate')
        End_Date = request.POST.get('EndDate')
        Description = request.POST.get('Description')

        Task_Details = TaskDetails(
            Task_Title=Task_Title,
            Task_Priority=Task_Priority,
            Start_Date=Start_Date,
            End_Date=End_Date,
            Description=Description,
        )
        Task_Details.save()
        return render(request, 'teamleadmodule/datainserted.html')
    return render(request, 'teamleadmodule/teamleadhomepage.html')

def view_task_details(request):
    task_details_list = TaskDetails.objects.all()
    return render(request, 'teamleadmodule/view_task_details.html', {'task_details_list': task_details_list})

def edit_task_details(request, task_id):
    task_details = get_object_or_404(TaskDetails, id=task_id)
    if request.method == 'POST':
        task_details.Task_Title = request.POST.get('TaskTitle')
        task_details.Task_Priority = request.POST.get('TaskPriority')
        task_details.Start_Date = request.POST.get('StartDate')
        task_details.End_Date = request.POST.get('EndDate')
        task_details.Description = request.POST.get('Description')
        task_details.save()
        return redirect('teamleadmodule:view_task_details')
    return render(request, 'teamleadmodule/edit_task_details.html', {'task_details': task_details})

def delete_task_details(request, task_id):
    task_details = get_object_or_404(TaskDetails, id=task_id)
    if request.method == 'POST':
        task_details.delete()
        return redirect('teamleadmodule:view_task_details')
    return render(request, 'teamleadmodule/delete_task_details.html', {'task_details': task_details})
