from rest_framework import serializers
from serial.models import SerialTest
from drf_extra_fields.fields import DateTimeRangeField

class SerialSerializer(serializers.ModelSerializer):

  first_name = serializers.SerializerMethodField()
  last_name = serializers.SerializerMethodField()
  
  start_date = serializers.SerializerMethodField()
  end_date = serializers.SerializerMethodField()

  def get_first_name(self, obj):
    return obj.full_name.split(" ")[0]

  def get_last_name(self, obj):
    return obj.full_name.split(" ")[1]

  def get_start_date(self, obj):
    return obj.date_range.lower

  def get_end_date(self, obj):
    return obj.date_range.upper

  class Meta:
        model = SerialTest
        fields = ('id', 'first_name', 'last_name', 'start_date', 'end_date')
