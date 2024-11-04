from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import SquaresDifference


@api_view(["GET"])
def difference(request: Request):

    given_number = int(request.query_params.get("number"))

    diff_data = get_object_or_404(SquaresDifference, given_number=given_number)

    response_data = {
        'datetime': timezone.now(),
        'value': diff_data.value,
        'number': given_number,
        'occurrences': diff_data.occurrences,
        'last_datetime': diff_data.last_requested,
    }

    # Update the number of occurrences
    # (this also auto-updates 'last_requested')
    diff_data.occurrences += 1
    diff_data.save()
    diff_data.refresh_from_db()

    return Response(response_data)
