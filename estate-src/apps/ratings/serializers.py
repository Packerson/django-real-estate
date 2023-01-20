from rest_framework import serializers

from .models import Rating

"""
Serializers allow complex data such as querysets and model 
instances to be converted to native Python datatypes that 
can then be easily rendered into JSON, XML or other content 
types. Serializers also provide deserialization, allowing 
parsed data to be converted back into complex types, after 
first validating the incoming data."""


class RatingSerializers(serializers.ModelSerializer):
    rater = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]

    """
     function connected with field has to have name:
    get_field
    """
    def get_rater(self, obj):
        return obj.rater.username

    def get_agent(self, obj):
        return obj.agent.user.username

