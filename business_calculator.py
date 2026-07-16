# customer_name = input("Customer Name: ")
# cloth_weight = float(input("Clothes Weight (kg): "))
# price_per_kg = float(input("Price per kg: "))

# total = cloth_weight * price_per_kg

# print("Customer:", customer_name)
# print("Total Bill:", total)

# customer_name = input("Customer Name: ")
# total_amount = float(input("Enter Amount: "))
# gst = total_amount * 18 / 100
# print(gst)

# customer_name = input("Customer Name: ")
# total_amount = float(input("Enter Amount: "))

# gst = total_amount * 18 / 100
# final_amount = total_amount + gst

# print("------------------------")
# print("Customer Name :", customer_name)
# print("Amount        :", total_amount) 
# print("GST (18%)     :", gst)
# print("Final Amount  :", final_amount)
# print("------------------------")

customer_name = input("Customer Name: ")
customer_bill_no = input("Enter Bill Number: ")
clothes_weight = float(input("Clothes Weight (kg): "))
price_per_kg = float(input("Price per KG: "))
total_amount = clothes_weight * price_per_kg
gst = total_amount *18 /100
full_amount = total_amount + gst
print("Customer Name :", customer_name)
print("Bill Number   :", customer_bill_no)
print("Weight (kg)   :", clothes_weight)
print("Price per KG  :", price_per_kg)
print("Total Amount  :", total_amount)
print("Final Amount  :", full_amount)
print("GST (18%)    :", gst)