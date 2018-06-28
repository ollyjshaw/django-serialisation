from serial.models import SerialTest
from serial.serializers import SerialSerializer
from rest_framework import generics
from datetime import datetime
from psycopg2.extras import DateTimeTZRange


class SerialList(generics.ListCreateAPIView):
    queryset = SerialTest.objects.all()
    serializer_class = SerialSerializer

    def perform_create(self, serializer):
      first_name = self.request.data['first_name']
      last_name = self.request.data['last_name']
      full_name = first_name + " " + last_name
      lower = datetime.strptime(self.request.data['start_date'], "%Y-%m-%d %H:%M")
      upper = datetime.strptime(self.request.data['end_date'], "%Y-%m-%d %H:%M")
      serializer.save(full_name=full_name, date_range=DateTimeTZRange(lower, upper, '(]'))
