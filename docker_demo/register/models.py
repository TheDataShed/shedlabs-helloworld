from __future__ import unicode_literals

from django.db import models

class Attendee(models.Model):
	first_name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	company = models.CharField(max_length=200)
	email_address = models.CharField(max_length=200)
	signed_up = models.DateTimeField('signed up')

