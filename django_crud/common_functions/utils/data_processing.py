def format_serializer_response(serializer, has_validated=False):
    if has_validated:
        return serializer.validated_data

    formatted_errors = []
    for field, errors in serializer.errors.items():
        formatted_errors.extend([{"field": field, "message": error} for error in errors])

    return {"errors": formatted_errors}


def format_response(response):
    return response
