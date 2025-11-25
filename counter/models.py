import hashlib
from django.db import models


class Quote(models.Model):
    text = models.CharField(max_length=2000)
    days_count = models.IntegerField()
    submission_time = models.DateTimeField(auto_now_add=True)
    ip_hash = models.CharField(max_length=64)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:50]

    @staticmethod
    def hash_ip(ip_address):
        """Hash an IP address using SHA-256."""
        return hashlib.sha256(ip_address.encode()).hexdigest()
