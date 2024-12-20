from django.db.models import Sum, Count

def get_top_categories():
    # Import models
    from .models import Category, Product

    # Query to get the top 5 categories by total product price
    top_categories = (
        Category.objects
        .annotate(
            total_price=Sum('product__price'),
            product_count=Count('product')
        )
        .filter(total_price__isnull=False)
        .order_by('-total_price')[:5]
    )

    # Formatting the result as a list of dictionaries
    result = [
        {
            "category_name": category.name,
            "total_price": category.total_price,
            "product_count": category.product_count
        }
        for category in top_categories
    ]

    return result

# Example usage
if __name__ == "__main__":
    output = get_top_categories()
    for item in output:
        print(item)