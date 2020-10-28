from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class JobListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobListing
        fields = ['title', 'company_name', 'description', 'job_location']
