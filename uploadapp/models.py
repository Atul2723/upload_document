from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model



class CustomUser(AbstractUser):
    pass

User = get_user_model()

class IPOChecklist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    share_certificates = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    allotment_docs = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    valuation_report = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    share_transfer_forms = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    share_purchase_agreement = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    gift_deed = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    
    register_members = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    register_allotment = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    register_charge = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    register_investment = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    register_loans_advances = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    register_directors = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    register_egm = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    register_transfer_transmission = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    register_related_party = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    fixed_asset_register = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    register_interest_director = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)

    minutes_signed = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    moa_word = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    moa_pdf = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)

    incorporation_certificate = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    roc_forms_pre_2006 = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    preferential_allotment_docs = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    central_govt_approval = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    roc_forms_post_ipo = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)
    borrowing_power_forms = models.FileField(upload_to='ipo_uploads/', blank=True, null=True)

    uploaded_at = models.DateTimeField(auto_now=True)


class Document(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='ipo_uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
