from .models import STATUS, Product

def set_product_availability(product, status):
    # Check that status is one of the correct types in STATUS key.
    status_initials = [initial[0] for initial in STATUS]

    if status in status_initials:
        product.loan_status = status
        product.save()


def set_current_borrower(product, user):
    product.current_borrower = user
    product.save()
