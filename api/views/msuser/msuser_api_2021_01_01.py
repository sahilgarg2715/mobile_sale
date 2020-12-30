from rest_framework import generics, status
from rest_framework.response import Response


class ManageMSUser_API_2021_01_01(generics.GenericAPIView):
    # authentication_classes = (MSBasicAuthentication,)
    # permission_classes = (IsAdminTeamMember,)

    def get(self, request):
        return Response(
            {"result": "Hello from get"},
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        return Response(
            {"result": "Hello from post"},
            status=status.HTTP_200_OK,
        )
