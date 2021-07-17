from rest_framework import generics, viewsets, status 
from rest_framework.response import Response
from .models import Labour, Job
from .serializers import LabourSerializer, JobSerializer

#imports for sms client .
import os
from twilio.rest import Client
account_sid = os.environ.get('account_sid')
auth_token  = os.environ.get('auth_token')
client = Client(account_sid, auth_token)



class LabourViewSet(viewsets.ModelViewSet):
     serializer_class = LabourSerializer
     queryset = Labour.objects.all()

     def create(self, request, *args, **kwargs):
          serializer = self.get_serializer(data=request.data)
          # message = client.messages \
          #       .create(
          #            body='''
          #                Congratulations  {0}   !
          #                You have been registered on sandhi portal with Aadhar No. {1} .
          #                All the Best !

          #                - Regards 
          #                     Team Sandhi 
          #            '''.format(request.data['first_name'],request.data['aadhar_number'] ) ,

          #            from_='+14703471874',
          #            to="+91" + str(request.data['contact_number'])
          #        )

          # print(message.sid)
          
          serializer.is_valid(raise_exception=True)
          self.perform_create(serializer)
          headers = self.get_success_headers(serializer.data)
          return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SkillBasedLabourListViewSet(generics.ListAPIView):
     serializer_class = LabourSerializer
     def get_queryset(self) : 
          return Labour.objects.all().filter(skill=self.kwargs['skill'])


class LocationSkillBasedJobListViewSet(generics.ListAPIView):
     serializer_class = JobSerializer
     def get_queryset(self) : 
          return Job.objects.all().filter(location=self.kwargs['location'] , skill_required=self.kwargs['skill'])



class JobViewSet(viewsets.ModelViewSet):
     serializer_class = JobSerializer
     queryset = Job.objects.all()


