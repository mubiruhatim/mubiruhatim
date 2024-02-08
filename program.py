
cost_price=int(input("ENTER COST PRICE: "))
transport_costs=int(input("ENTER TRANSPORT COST: "))
selling_price =(cost_price + (5/100)*cost_price + (2/100)*transport_costs)

profit=(selling_price-cost_price)
print(f"SELLING PRICE IS UGX\t{selling_price}\nPROFIT IS UGX\t{profit}")