from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class API_VERSIONS:
    API_VERSION_2021_01_01 = "api_2021_01_01"

    HEADER_NAME = "X-MS-API-Version"

    API_VERSIONS = [
        API_VERSION_2021_01_01,
    ]
    CURRENT_VERSION = API_VERSION_2021_01_01

    def get_api_version(self, headers):
        header = headers.get(self.HEADER_NAME)
        if header is None:
            # the first version of the app didn't have API versioning
            return True, self.API_VERSION_2021_01_01
        elif header in self.API_VERSIONS:
            return True, header
        else:
            # error, given version doesn't exist
            response = (
                Response(
                    {
                        "http_status_code": "403",
                        "message": "given version doesn't exist",
                        "component_on_error": "API_VERSIONING",
                        "ms_error_code": "1001",
                    },
                    content_type="application/json",
                    status=status.HTTP_403_FORBIDDEN,
                ),
            )
            (error_response,) = response
            error_response.accepted_renderer = JSONRenderer()
            error_response.accepted_media_type = "application/json"
            error_response.renderer_context = {}
            return (False, error_response)
