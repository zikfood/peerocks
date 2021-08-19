from rest_framework.renderers import (
    JSONOpenAPIRenderer as DRFJSONOpenAPIRenderer,
)
from rest_framework.utils import (
    json,
)


class JSONOpenAPIRenderer(DRFJSONOpenAPIRenderer):
    def render(self, data, media_type=None, renderer_context=None):
        result = json.dumps(
            data,
            indent=2,
        ).replace(
            '\\\\Z',
            '$',
        ).encode(
            'utf-8',
        )

        return result
