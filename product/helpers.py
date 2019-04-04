from .models import STATUS, Product

def set_product_availability(product, status):
    status_initials = [initial[0] for initial in STATUS]

    if status in status_initials:
        product.loan_status = status
        product.save()
