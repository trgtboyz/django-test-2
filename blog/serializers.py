from rest_framework import serializers
from .models import ContactDetails

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = "__all__"
