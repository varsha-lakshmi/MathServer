# Ex.04 Design a Website for Server Side Processing
## Date:

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
<html>
<head>
    <title>GST Calculator</title>
</head>
<body>

    <form method="post">
    <h2>GST Calculator</h2>

        {% csrf_token %}
        <label for="price">Price :</label>
        <input type="text" name="price" required><br><br>

        <label for="gst">GST (%):</label>
        <input type="text" name="gst" required><br><br>

        <button type="submit">Calculate</button>
    </form>

    {% if gst_amt is not None %}
        <h2>Result:</h2>
        {% if "Error" in gst_amt|stringformat:"s" %}
            <p style="color: red;">{{ gst_amt }}</p>
        {% else %}
            <p>GST: {{ gst_amt|stringformat:".2f" }}</p>
        {% endif %}
    {% endif %}
</body>
</html>
```
```
from django.shortcuts import render

def gst_amt_calc(request):

    gst_amt = None

    if request.method == 'POST':

        try:
            price = float(request.POST.get('price'))
            gst = float(request.POST.get('gst'))

            if price >= 0 and gst >= 0:

                gst_amt = price + ((price * gst) / 100)

            else:
                gst_amt = "Error: Inputs cannot be negative."

        except ValueError:

            gst_amt = "Error: Please enter valid numbers."

    context = {
        'gst_amt': gst_amt
    }

    return render(request, 'bill.html', context)
    ```
    ```
    from django.contrib import admin
from django.urls import path
from billapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.gst_amt_calc, name='gst_amt'),
]
```


## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2026-06-01 102752.png>)

## OUTPUT - WEBPAGE:

![alt text](<Screenshot 2026-06-01 102736.png>)
## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
