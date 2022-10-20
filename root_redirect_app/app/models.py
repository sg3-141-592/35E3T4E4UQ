from django.db import models
from django.utils.translation import gettext_lazy as _

class Site(models.Model):
    source_url = models.CharField(max_length=2048)
    target_url = models.CharField(max_length=2048)
    private_key = models.TextField()
    fullchain_key = models.TextField()

    class ProvisioningState(models.TextChoices):
        ONE_GET_URL = '1-GET-USER-URL', _('1 - Get user urls'),
        TWO_ADD_A_RECORD = '2-ADD-A-RECORD', _('2 - Add A record'),
        THREE_CHECK_A_RECORD = '3-CHECK-A-RECORD', _('3 - Checking A record mapping'),
        FOUR_GENERATE_CERT = '4-GENERATE-CERT', _('4 - Generating certificate')
        FIVE_TEST_CERT = '5-TEST-CERT', _('5 - Testing SSL certificate'),
        SIX_TEST_REDIRECT = '6-TEST-REDIRECT', _('6 - Testing redirect'),
        VALID = "VALID", _('Valid entry')
    
    provisioning_state = models.CharField(
        max_length=32,
        choices = ProvisioningState.choices,
        default = ProvisioningState.ONE_GET_URL
    )

    # Debug text
    a_record_state = models.TextField()

    def __str__(self):
        return f"{self.source_url} - {self.target_url} - {self.provisioning_state}"
