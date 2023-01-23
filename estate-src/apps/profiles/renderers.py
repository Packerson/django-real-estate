import json

from rest_framework.renderers import JSONRenderer


class ProfileJSONRenderer(JSONRenderer):
    charset = "utf-8"

    """ define function to override JSONRenderer to render profile data 
    and namespaces """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(ProfileJSONRenderer, self).render(data)

        """if everything is ok return profile with data"""
        return json.dumps({"profile": data})
