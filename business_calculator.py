print("======================================")
print("      KLYN LAUNDRY & DRYCLEANING")
print("======================================")

# Customer Details
customer_name = input("Customer Name      : ")
customer_bill_no = input("Enter Bill Number  : ")
customer_phone = input("Phone Number       : ")

# Laundry Details
clothes_weight = float(input("Clothes Weight (kg): "))
price_per_kg = float(input("Price per KG       : "))

# Calculations
total_amount = clothes_weight * price_per_kg
gst = total_amount * 18 / 100
final_amount = total_amount + gst

# Final Bill
print("\n======================================")
print("            CUSTOMER BILL")
print("======================================")
print("Customer Name   :", customer_name)
print("Bill Number     :", customer_bill_no)
print("Phone Number    :", customer_phone)
print("--------------------------------------")
print("Weight (kg)     :", clothes_weight)
print("Price per KG    :", price_per_kg)
print("Total Amount    :", total_amount)
print("GST (18%)       :", gst)
print("Final Amount    :", final_amount)
print("======================================")
print(" Thank You! Visit Again.")
print("======================================")