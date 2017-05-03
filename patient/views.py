from django.shortcuts import render
from django.shortcuts import  render_to_response

from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import BasicAuthentication

# Create your views here.

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

class DisableCSRF(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)

def main(request):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    return render_to_response('patient/index.html')



