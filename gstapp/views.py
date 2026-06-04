from django.shortcuts import render

def gst(request):
    bill = None

    if request.method == "POST":
        price = float(request.POST["price"])
        gst_percent = float(request.POST["gst"])

        gst_amount = (price * gst_percent) / 100
        bill = price + gst_amount

    return render(request, "gstapp/gst.html", {"bill": bill})