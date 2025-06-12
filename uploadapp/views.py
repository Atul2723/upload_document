from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Document
from .forms import DocumentUploadForm
from .forms import CustomUserCreationForm
from .models import IPOChecklist
from .forms import IPOChecklistForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('document_upload')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('document_upload')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def document_upload(request):
    user = request.user
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            Document.objects.update_or_create(
                user=user,
                field_name=form.cleaned_data['field_name'],
                defaults={'file': form.cleaned_data['file']}
            )
            return JsonResponse({'message': 'File uploaded'}, status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)

    uploaded_docs = Document.objects.filter(user=user)
    uploaded_fields = {doc.field_name for doc in uploaded_docs}
    all_fields = [
        'share_certificates', 'allotment_docs', 'valuation_report',
        'share_transfer_forms', 'share_purchase_agreement', 'gift_deed',
        'register_members', 'register_allotment', 'register_charge',
        'register_investment', 'register_loans_advances', 'register_directors',
        'register_egm', 'register_transfer_transmission', 'register_related_party',
        'fixed_asset_register', 'register_interest_director', 'minutes_signed',
        'moa_word', 'moa_pdf', 'incorporation_certificate', 'roc_forms_pre_2006',
        'preferential_allotment_docs', 'central_govt_approval',
        'roc_forms_post_ipo', 'borrowing_power_forms'
    ]
    return render(request, 'upload.html', {
        'user': user,
        'uploaded_docs': uploaded_docs,
        'all_fields': all_fields,
        'uploaded_fields': uploaded_fields
    })



@login_required
def checklist_upload_view(request):
    instance = IPOChecklist.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = IPOChecklistForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('checklist_upload')
    else:
        form = IPOChecklistForm(instance=instance)

    return render(request, 'checklist_upload.html', {
        'form': form,
        'user': request.user
    })