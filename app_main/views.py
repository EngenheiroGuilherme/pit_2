from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

# List tasks
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

# Create task
def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('list_tasks')
    return render(request, 'task_form.html')

# Update task
def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = 'status' in request.POST
        task.save()
        return redirect('list_tasks')
    return render(request, 'task_form.html', {'task': task})

# Delete task
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('list_tasks')


from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Task

def generate_pdf(request):
    # Cria a resposta HTTP para o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="task_list.pdf"'

    # Configurando o PDF
    pdf = canvas.Canvas(response)
    pdf.setFont("Helvetica", 14)
    pdf.drawString(100, 800, "Task List")
    pdf.setFont("Helvetica", 12)

    # Buscando as tarefas
    y = 750
    tasks = Task.objects.all()
    for task in tasks:
        status = "Completed" if task.status else "Pending"
        pdf.drawString(100, y, f"Title: {task.title}, Description: {task.description}, Status: {status}")
        y -= 20

    # Finaliza o PDF
    pdf.save()
    return response
