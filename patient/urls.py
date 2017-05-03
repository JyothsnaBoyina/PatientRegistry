from django.conf.urls import url
from patient import api

from patient import views

urlpatterns=[

url(r'^$',views.main),
url(r'^api/patient/$',api.patient_view1),
url(r'^api/patient/(?P<pk>[0-9]+)/$',api.patient_view),

]