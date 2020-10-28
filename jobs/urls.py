
from django.urls import path
from .views import *

app_name = 'jobs'

urlpatterns = [

    path('article/<int:pk>/', PostDetailView.as_view(), name="govtpv"),

    path('contact/', contact, name='contact'),
    path('about/', about_us, name='about'),
    path('service/', service, name='service'),
    path('job-post/', job_post, name='job-post'),
    path('job-listing/', job_listing, name='job-listing'),
    path('govt/', govt, name='govt'),
    path('govtpv/', govt, name='govtpv'),
    path('job-single/<int:id>/', job_single, name='job-single'),
    path('search/', SearchView.as_view(), name='search'),
    path('apply/', apply_job, name='apply'),

]
