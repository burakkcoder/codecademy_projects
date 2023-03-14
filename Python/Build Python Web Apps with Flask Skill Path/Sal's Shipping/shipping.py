weight = 5

#Ground Shipping
if weight <= 2:
    cost_ground = (weight * 1.5) + 20
elif weight > 2 and weight <= 6:
    cost_ground = (weight * 3) + 20
elif weight > 6 and weight <= 10:
    cost_ground = (weight * 4) + 20
elif weight > 10:
    cost_ground = (weight * 4.75) + 20

print(f"Ground Shipping Cost : ${cost_ground}")

#Ground Shipping Premium
cost_ground_premium = 125

print(f"Ground Shipping Premium Cost : ${cost_ground_premium}")

#Drone Shipping
if weight <= 2:
    cost_drone = weight * 4.5
elif weight > 2 and weight <= 6:
    cost_drone = weight * 9
elif weight > 6 and weight <= 10:
    cost_drone = weight * 12
elif weight > 10:
    cost_drone = weight * 14.25

print(f"Drone Shipping Cost : ${cost_drone}")