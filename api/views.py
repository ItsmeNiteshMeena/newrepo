from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer

class TaskAPIView(APIView):

    def get(self, request):
        # GET method just returns operation_code
        return Response({"operation_code": "OP1234"}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            # find highest alphabet
            highest_alpha = max(data['alphabets'])
            return Response({
                "status": "success",
                "user_id": data['user_id'],
                "college_email": data['college_email'],
                "college_roll_number": data['college_roll_number'],
                "numbers": data['numbers'],
                "alphabets": data['alphabets'],
                "highest_alphabet": highest_alpha
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

