from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UploadedFile
from django.contrib.auth.models import User
from .models import UploadedFile, SharedFile

@login_required
def dashboard(request):
    user_files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'user_files': user_files})

@login_required
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        UploadedFile.objects.create(user=request.user, file=uploaded_file)
        return redirect('dashboard')
    return render(request, 'upload_file.html')

@login_required
def dashboard(request):
    user_files = UploadedFile.objects.filter(user=request.user)
    shared_files = SharedFile.objects.filter(shared_with=request.user)
    return render(request, 'dashboard.html', {'user_files': user_files, 'shared_files': shared_files})

@login_required
def search_users(request):
    query = request.GET.get('q')
    results = User.objects.filter(username__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})

@login_required
def share_file(request, file_id):
    file_to_share = UploadedFile.objects.get(id=file_id)
    shared_with_username = request.POST.get('shared_with')
    shared_with_user = User.objects.get(username=shared_with_username)
    
    if not SharedFile.objects.filter(file=file_to_share, shared_with=shared_with_user).exists():
        SharedFile.objects.create(file=file_to_share, shared_with=shared_with_user)

    return redirect('dashboard')