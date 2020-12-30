from rest_framework import generics
from ...api_versions import API_VERSIONS
from ...logger import logger, LogRecord
from .msuser_api_2021_01_01 import ManageMSUser_API_2021_01_01

class APIEndpointView(generics.GenericAPIView):
    version_classes = {}  # derived classes should override this.

    def dispatch(self, request, *args, **kwargs):
        log_record_obj = LogRecord()

        # Decide which version to invoke.
        is_success, version_or_error = API_VERSIONS().get_api_version(
            self.request.headers
        )
        if not is_success:
            log_record = log_record_obj.createRecord(
                module="MSUSER_APIs",
                event="INVALID_API_VERSION",
                creator_user=self.request.user,
                errors=version_or_error.data,
            )
            logger.error("INVALID_API_VERSION", log_record)
            return version_or_error

        # If version is not specified return oldest version which is default
        if version_or_error not in self.version_classes:
            return version_or_error

        # Get the *actual* view class that implements this version
        view_class = self.version_classes[version_or_error]

        # Instantiate and invoke the actual view, returning its value
        actual_view = view_class.as_view()
        return actual_view(request, *args, **kwargs)


class ManageMSUser(APIEndpointView):
    version_classes = {
        API_VERSIONS.API_VERSION_2021_01_01: ManageMSUser_API_2021_01_01,
    }
