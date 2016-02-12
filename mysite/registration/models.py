from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class BuildUserInformation(models.Model):
    first_name = models.NullBooleanField('first name', False)
    last_name = models.NullBooleanField('last name', False)



class Company(models.Model):
    """Company account in Reggie"""

    company_name = models.CharField(max_length=100)
    company_email = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=30)
    company_address = models.CharField(max_length=300)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        """Provides helpful representation when printed"""

        return self.company_name



class User(models.Model):
    """User account in Reggie"""
   
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=30)
    user_address = models.CharField(max_length=300)
    password = models.CharField(max_length=20)

    def __str__(self):
        """Provides helpful representation when printed"""

        return self.user_id, self.user_name, self.user_email



class Event(models.Model):
    """Event in Reggie"""

    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


    def __str__(self):
        """Provides helpful representation when printed"""

        return self.event_id, self.event_name, self.company_id


class UserEvent(models.Model):
    """User events in Reggie"""

    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        """Provides helpful representation when printed"""

        return self.user_event_id

