from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ..views import (
    ManageMSUser,
)

urlpatterns = {path("msusers", ManageMSUser.as_view(), name="create-or-getall-ms-user")}

# The format_suffix_pattern allows us to specify the data format (raw json or even html) when we use the URLs.
# It appends the format to be used to every URL in the pattern.
msuser_urlpatterns = format_suffix_patterns(urlpatterns)
