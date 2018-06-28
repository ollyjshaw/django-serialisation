from rest_framework import serializers
from serial.models import SerialTest
from drf_extra_fields.fields import DateTimeRangeField

class NameField(serializers.Field):
  def to_representation(self, obj):
    ret = {
      "first_name": obj.full_name.split(" ")[0],
      "last_name": obj.full_name.split(" ")[1]
    }
    return ret
  
  def to_internal_value(self, data):
    ret = {
      "full_name": data["first_name"] + data["last_name"]
    }
    return ret

class SerialSerializer(serializers.ModelSerializer):
  
  full_name = NameField(source='*')

  start_date = serializers.SerializerMethodField()
  end_date = serializers.SerializerMethodField()

  def get_start_date(self, obj):
    return obj.date_range.lower

  def get_end_date(self, obj):
    return obj.date_range.upper

  class Meta:
        model = SerialTest
        fields = ('id', 'full_name', 'start_date', 'end_date')
