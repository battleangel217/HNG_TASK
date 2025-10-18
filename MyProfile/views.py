from django.shortcuts import render
from rest_framework.views import APIView, status, Response
from django.utils import timezone
import requests

# Create your views here.


class ProfileViews(APIView):
    def get(self, request):
        try:
            response = requests.get('https://catfact.ninja/fact')
        except requests.Timeout:
            return Response({'status': 'error', 'message': 'The request timed out.'}, status=504)

        except requests.ConnectionError:
            return Response({'status': 'error', 'message': 'Network connection error.'}, status=502)

        except requests.HTTPError as e:
            return Response({
                'status': 'error',
                'message': f'HTTP error: {e.response.status_code}'
            }, status=e.response.status_code)

        except requests.RequestException as e:
            return Response({'status': 'error', 'message': str(e)}, status=500)
        
        fact = response.json()
        info = {
            "status":"success",
            "user": {
                "email":"idaraobong05@gmail.com",
                "name": "Etim, Idaraobong Joseph",
                "stack": "Python/Django"
            },
            "timestamp": timezone.now(),
            "fact": fact["fact"]
        }
        return Response(info, status=status.HTTP_200_OK)