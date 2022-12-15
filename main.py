
# Fall Damage Calculator

# Import necessary libraries
import math

# Define velocity formula
def velocity(height):
  v = math.sqrt(2 * g * height)
  return v

# Define function to calculate survival percentage
def survival_percentage(velocity, weight, clothing_thickness, floor_type):
  # Assume initial survival percentage is 100%
  survival_percentage = 100

  # Calculate fall velocity and apply survival rates based on velocity
  if velocity <= 60:
    survival_percentage -= 20
  elif velocity <= 90:
    survival_percentage -= 30
  elif velocity <= 120:
    survival_percentage -= 50
  else:
    survival_percentage = 0

  # Apply additional survival rates based on weight
  if weight <= 120:
    survival_percentage -= 10
  elif weight <= 150:
    survival_percentage -= 20
  elif weight <= 180:
    survival_percentage -= 30
  else:
    survival_percentage -= 40

  # Apply additional survival rates based on clothing thickness
  if clothing_thickness <= 1:
    survival_percentage -= 10
  elif clothing_thickness <= 2:
    survival_percentage -= 20
  elif clothing_thickness <= 3:
    survival_percentage -= 30
  else:
    survival_percentage -= 40

  # Apply additional survival rates based on floor type
  if floor_type == "concrete":
    survival_percentage -= 30
  elif floor_type == "asphalt":
    survival_percentage -= 20
  elif floor_type == "grass":
    survival_percentage -= 10
  else:
    survival_percentage -= 40

  # Return final survival percentage
  return survival_percentage

# Define global variable for gravitational constant
g = 9.81

# Prompt user for input
height = float(input("Enter height of fall in feet: "))
weight = float(input("Enter weight of person in pounds: "))
clothing_thickness = float(input("Enter thickness of clothing in inches: "))
floor_type = input("Enter type of floor (concrete, asphalt, grass, other): ")

# Calculate fall velocity
v = velocity(height)

# Calculate and print survival percentage
survival_pct = survival_percentage(v, weight, clothing_thickness, floor_type)
print(f"Survival percentage: {survival_pct}%")

# Add a disclaimer about the use of this program
print("This program is for informational purposes only and should not be used to determine actual survival rates in real-world falls.")
