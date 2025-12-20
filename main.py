AVG_FUEL_CONSUMPTION = 6.9/100
distance_trip = float(input("Enter the distance (km): "))
price_fuel = float(input("Enter the price of fuel ($/L): "))

if distance_trip <= 0 or price_fuel <= 0:
  print("Invalid Input")
  exit()

driving_type = input("Enter driving type (C for city driving and H for highway): ").upper()

if driving_type not in("C", "H"):
  print("Invalid Input, enter either 'C' or 'H' only")

if driving_type == 'C':
  fuel_consumption = (0.15*(AVG_FUEL_CONSUMPTION)) + AVG_FUEL_CONSUMPTION
else:
  fuel_consumption = AVG_FUEL_CONSUMPTION - (0.10*(AVG_FUEL_CONSUMPTION))

fuel_used = distance_trip*fuel_consumption

base_cost = price_fuel*fuel_used

if price_fuel > 1.6:
  total_cost = base_cost*0.05
else:
  total_cost = base_cost

print(f"Total fuel used: {fuel_used:.2f}\nTotal trip fuel cost: ${total_cost:.2f}")