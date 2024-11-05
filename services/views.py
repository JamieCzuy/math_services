from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import (
    SquaresDifference,
    Triplet,
)


@api_view(["GET"])
def difference(request: Request):

    try:
        given_number = int(request.query_params.get("number"))
        not_an_int = False
    except Exception:
        not_an_int = True

    if not_an_int or given_number < 0 or given_number > 100:
        msg = ("Query parameter 'number' is required and must be an integer that is"
               " greater than or equal to 0 and less than or equal to 100!")

        return Response(msg, status=400)

    diff_data = get_object_or_404(SquaresDifference, given_number=given_number)

    current_datetime = timezone.now()
    response_data = {
        'datetime': current_datetime,
        'value': diff_data.value,
        'number': given_number,
        'occurrences': diff_data.occurrences,
        'last_datetime': diff_data.last_requested,
    }

    # Update the number of occurrences
    # and last requested timestamp
    diff_data.occurrences += 1
    diff_data.last_requested = current_datetime

    diff_data.save()
    diff_data.refresh_from_db()

    return Response(response_data)


@api_view(["GET"])
def triplet(request: Request):

    # Verify the request
    try:
        a = int(request.query_params.get("a"))
        b = int(request.query_params.get("b"))
        c = int(request.query_params.get("c"))
        all_ints = True
    except Exception:
        all_ints = False

    if not all_ints:
        msg = "Query parameters 'a', 'b' and 'c' are required and must be integers"
        return Response(msg, status=400)

    triplet = Triplet.get_or_create(a, b, c)

    current_datetime = timezone.now()
    response_data = {
        'datetime': current_datetime,
        'a': triplet.a,
        'b': triplet.b,
        'c': triplet.c,
        'is_triplet': triplet.is_triplet,
        'product': triplet.product,
        'occurrences': triplet.occurrences,
        'last_datetime': triplet.last_requested,
    }

    return Response(response_data)
