# Ex.04 Design a Website for Server Side Processing

## Date:

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)

- P → Price (in Rupees)
- GST → GST (in Percentage)
- Bill → Total Bill Amount (in Rupees)

## DESIGN STEPS:

1. Clone the repository from GitHub.
2. Create a Django admin project.
3. Create a new app under the Django project.
4. Create an HTML template for form input and output.
5. Create view and URL handlers for server-side processing.
6. Receive input values from the form using `request.POST.get()`.
7. Calculate the total bill amount including GST.
8. Render the calculated result to the HTML template.
9. Publish the website on localhost.

## PROGRAM:

### Template (`gstapp/templates/gstapp/gst.html`)
```html
<!DOCTYPE html>
<html>
<head>
    <title>GST Bill Calculator</title>
</head>
<body>

    <h1>GST Bill Calculator</h1>

    <form method="post">
        {% csrf_token %}

        <label>Price:</label>
        <input type="number" name="price" required>
        <br><br>

        <label>GST Percentage:</label>
        <input type="number" name="gst" required>
        <br><br>

        <button type="submit">Calculate</button>
    </form>

    {% if bill %}
        <h2>Total Bill Amount = ₹ {{ bill }}</h2>
    {% endif %}

</body>
</html>
```

### View (`gstapp/views.py`)
```python
from django.shortcuts import render

def gst(request):
    bill = None

    if request.method == 'POST':
        price = float(request.POST['price'])
        gst_percent = float(request.POST['gst'])
        gst_amount = (price * gst_percent) / 100
        bill = price + gst_amount

    return render(request, 'gstapp/gst.html', {'bill': bill})
```

### URLs (`gstapp/urls.py`)
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gst, name='gst'),
]
```

### Project URLs (`mathserver/urls.py`)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gstapp.urls')),
]
```

## OUTPUT - SERVER SIDE:
<img width="1073" height="311" alt="Screenshot 2026-06-04 235129" src="https://github.com/user-attachments/assets/b8555e8d-5784-4fc4-a895-d5f0c883e86b" />


## OUTPUT - WEBPAGE:
<img width="1090" height="557" alt="Screenshot 2026-06-04 234634" src="https://github.com/user-attachments/assets/d3c63158-ddca-4e3a-aad7-2b46a01e766a" />


## RESULT:
A web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
