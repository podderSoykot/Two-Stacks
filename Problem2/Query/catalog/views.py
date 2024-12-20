from django.http import HttpResponse
from django.db.models import Sum, Count
from .models import Category, Product

def top_categories(request):

    categories = Category.objects.annotate(
        total_price=Sum('products__price'),
        product_count=Count('products')
    ).filter(product_count__gt=0).order_by('-total_price')[:5]
    
    category_data = [
        {
            'category_name': category.name,
            'total_price': category.total_price,
            'product_count': category.product_count
        }
        for category in categories
    ]

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Top Categories</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            h1 {
                text-align: center;
                margin-top: 30px;
                color: #333;
            }
            table {
                width: 80%;
                margin: 30px auto;
                border-collapse: collapse;
                background-color: #fff;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            th, td {
                padding: 12px;
                text-align: center;
                border: 1px solid #ddd;
            }
            th {
                background-color: #4CAF50;
                color: white;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            tr:hover {
                background-color: #ddd;
            }
            td {
                font-size: 14px;
            }
            .currency {
                color: #28a745;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1>Top 5 Categories by Total Product Price</h1>
        
        <table>
            <thead>
                <tr>
                    <th>Category Name</th>
                    <th>Total Price</th>
                    <th>Product Count</th>
                </tr>
            </thead>
            <tbody>
    """

    for category in category_data:
        html_content += f"""
            <tr>
                <td>{category['category_name']}</td>
                <td><span class="currency">${category['total_price']}</span></td>
                <td>{category['product_count']}</td>
            </tr>
        """
    
    html_content += """
            </tbody>
        </table>
    </body>
    </html>
    """
    
    return HttpResponse(html_content)


