from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .forms import JobForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


@login_required
def dashboard(request):

    jobs = Job.objects.filter(user=request.user)

    context = {
        'jobs': jobs,
        'total': jobs.count(),
        'interviews': jobs.filter(status='Interview').count(),
        'offers': jobs.filter(status='Offer').count(),
        'rejected': jobs.filter(status='Rejected').count(),
    }

    return render(request, 'dashboard.html', context)


@login_required
def add_job(request):

    if request.method == 'POST':

        form = JobForm(request.POST)

        if form.is_valid():

            job = form.save(commit=False)

            job.user = request.user

            job.save()

            return redirect('dashboard')

    else:
        form = JobForm()

    return render(request, 'add_job.html', {'form': form})


@login_required
def edit_job(request, pk):

    job = get_object_or_404(Job, pk=pk, user=request.user)

    if request.method == 'POST':

        form = JobForm(request.POST, instance=job)

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    else:
        form = JobForm(instance=job)

    return render(request, 'edit_job.html', {'form': form})


@login_required
def delete_job(request, pk):

    job = get_object_or_404(Job, pk=pk, user=request.user)

    job.delete()

    return redirect('dashboard')


def register(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('dashboard')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})