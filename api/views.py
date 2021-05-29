from api.serializers import BranchSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from api import models
from .serializers import BranchSerializer
from rest_framework.decorators import api_view, renderer_classes


# Create your views here.
@api_view(('GET',))
def search(request):
    ifsc = request.GET.get("ifsc") or ""
    branch = request.GET.get("branch") or ""
    bank_id = request.GET.get("bank_id") or ""
    address = request.GET.get("address") or ""
    city = request.GET.get("city") or ""
    district = request.GET.get("district") or ""
    state = request.GET.get("state") or ""
    bank_name = request.GET.get("bank_name") or ""
    limit = request.GET.get("limit") or 100
    limit = int(limit)
    branches = models.Branches.objects.filter(
        ifsc__icontains = ifsc,
        branch__icontains = branch,
        bank_id__icontains = bank_id,
        address__icontains = address,
        city__icontains = city,
        district__icontains = district,
        state__icontains = state,
        bank_name__icontains = bank_name
    )[:limit]
    serializer = BranchSerializer(branches, many = True)
    return Response(serializer.data)