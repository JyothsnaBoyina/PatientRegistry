from rest_framework.decorators import api_view
from patient.serializers import *
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from patient.views import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET', 'POST'])
def patient_view1(request,format=None):
    if request.method == 'GET':
        patients = Patients.objects.filter()
        serializer = PatientSerializer(patients,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def patient_view(request, pk,format=None):
    if request.method == 'GET':
        patients = Patients.objects.filter(id=pk)
        serializer = PatientSerializer(patients,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        patients = Patients.objects.filter(id=pk)
        serializer = PatientSerializer(patients, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        patients = Patients.objects.filter(id=pk)
        patients.delete()
        return Response(status=204)
