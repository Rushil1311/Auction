import razorpay


# Replace with your actual API keys
razorpay_key_id = "rzp_test_xxxxxxxx"  # or rzp_live_xxxxxxxx for live mode
razorpay_key_secret = "BmKT1rAvCcMTFrvCkX02DSpg"

client = razorpay.Client(auth=(razorpay_key_id, razorpay_key_secret))

try:
    response = client.order.all()
    print(response)
except Exception as e:
    print("Error:", e)
