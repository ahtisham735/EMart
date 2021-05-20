from .models import ShippingDetail
def is_detail_exist(user):
    try:
        details=ShippingDetail.objects.get(user=user)
        return details
    except ShippingDetail.DoesNotExist:
        return None