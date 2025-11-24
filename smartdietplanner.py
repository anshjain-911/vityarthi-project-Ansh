Limit = 2000
weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in m:"))
def bmifxn(weight,height):
   bmi = float(weight/(height**2))
   return bmi
bmi_value = bmifxn(weight,height)


def bmi_cat(bmi_value):
   
   if bmi_value <= 18.5:
     return "Underweight"
   elif 18.5 <= bmi_value <= 24.9:
      return "Normal weight"
   elif 25 <=bmi_value<= 29.9:
      return "Overweight"
   else:
      return "obese"
   
def cal_suggestion(total):
   if total < Limit/2:
      return"You are eating too little, try adding fruits or a proper meal"
   elif total< Limit:
      return"You can have a light snack if you're hungry"
   else:
      return"Calorie limit exceeded! Avoid having heavy meals, but a fruit or 2 wouldn't hurt if you're hungry"
   


category = bmi_cat(bmi_value)

print("Your bmi:" , bmi_value)
print("BMI category:" , category)

print("\n Now enter food you ate today:")
print("Type 'done' when you're finished.\n")

total_calories = 0
food_data = {
    # Fruits 
    "apple": 95,
    "banana": 105,
    "orange": 62,
    "mango": 150,
    "grapes (1 cup)": 104,
    "watermelon (1 cup)": 46,
    "papaya (1 cup)": 55,
    "pineapple (1 cup)": 82,
    "pomegranate (1 cup)": 144,
    "guava": 68,
    "strawberries (1 cup)": 53,
    "blueberries (1 cup)": 85,
    "kiwi": 42,
    "pear": 101,
    "cherry (1 cup)": 77,
    "fig": 47,
    "dates (1 piece)": 23,

    # Vegetables
    "carrot (1 cup)": 52,
    "broccoli (1 cup)": 55,
    "spinach (1 cup)": 23,
    "potato (boiled)": 87,
    "sweet potato": 112,
    "cauliflower (1 cup)": 25,
    "peas (1 cup)": 118,
    "corn (1 cup)": 140,
    "tomato": 22,
    "cucumber": 16,
    "onion (1)": 44,
    "beetroot (1 cup)": 58,
    "ladyfinger (1 cup)": 33,
    "cabbage (1 cup)": 22,
    "mushroom (1 cup)": 15,

    #Indian Home Meals 
    "chapati": 120,
    "paratha": 200,
    "aloo paratha": 260,
    "paneer paratha": 320,
    "rice (1 cup)": 130,
    "dal (1 cup)": 198,
    "rajma (1 cup)": 240,
    "chole (1 cup)": 280,
    "sambar (1 cup)": 100,
    "rasam (1 cup)": 60,
    "khichdi (1 cup)": 180,
    "curd (1 cup)": 100,
    "idli": 50,
    "dosa": 168,
    "uttapam": 180,
    "poha": 180,
    "upma": 250,
    "vada": 200,
    "pulao (1 cup)": 250,
    "biriyani (1 cup)": 300,
    "pav bhaji": 400,
    "thepla": 150,
    "dal makhani (1 cup)": 300,
    "paneer butter masala (1 cup)": 380,
    "butter chicken (1 cup)": 470,
    "kadhi (1 cup)": 130,
    "dhokla (2 pieces)": 160,

    # South Indian
    "masala dosa": 390,
    "plain dosa": 160,
    "idli sambar": 120,
    "medu vada": 200,
    "pongal": 220,
    "appam": 120,

    # North Indian
    "naan": 260,
    "butter naan": 300,
    "kulcha": 180,
    "aloo sabzi (1 cup)": 210,
    "baingan bharta (1 cup)": 190,
    "karela fry": 80,
    "paneer tikka": 270,

    #Snacks & Fast Food
    "samosa": 250,
    "kachori": 190,
    "pakoda (1 piece)": 75,
    "pani puri (1 plate)": 220,
    "bhel puri": 170,
    "sev puri": 260,
    "vada pav": 290,
    "puff": 250,
    "spring roll": 120,
    "fries (small)": 220,
    "burger": 300,
    "cheese burger": 350,
    "pizza slice": 285,
    "pasta (1 cup)": 220,
    "noodles (1 cup)": 190,
    "maggi": 350,
    "sandwich": 200,
    "grilled sandwich": 260,
    "momos (6 pcs)": 280,

    # Sweets & Desserts 
    "gulab jamun": 150,
    "rasgulla": 120,
    "jalebi (1 piece)": 150,
    "laddu": 180,
    "kheer (1 cup)": 250,
    "halwa (1 cup)": 300,
    "ice cream (1 scoop)": 137,
    "brownie": 250,
    "chocolate (1 bar)": 210,
    "cake slice": 250,

    # Bakery Items 
    "bread slice": 66,
    "butter (1 tbsp)": 102,
    "jam (1 tbsp)": 56,
    "croissant": 231,
    "bun": 120,
    "cookies (1 piece)": 50,

    # Breakfast 
    "cornflakes (1 cup)": 100,
    "oats (1 cup cooked)": 150,
    "omelette (2 eggs)": 180,
    "boiled egg": 78,
    "sandwich": 200,
    "peanut butter (1 tbsp)": 94,
    "milk (1 cup)": 100,
    "curd": 100,

    # Protein Foods 
    "egg": 78,
    "chicken (100g)": 250,
    "fish (100g)": 206,
    "paneer (100g)": 296,
    "tofu (100g)": 94,
    "soy chunks (1 cup)": 336,
    "rajma": 240,
    "chole": 280,

    #  Drinks & Beverages 
    "water": 0,
    "tea": 30,
    "coffee": 40,
    "milkshake": 220,
    "cold coffee": 200,
    "coke can": 140,
    "sprite can": 140,
    "juice glass": 120,
    "buttermilk": 80,
    "lassi": 260,
    "energy drink": 110,

    # Dry Fruits
    "almonds (10)": 70,
    "cashews (10)": 90,
    "walnuts (5)": 130,
    "raisins (1 tbsp)": 30,
    "peanuts (1 handful)": 160,

    # Other Misc. Foods 
    "cheese slice": 113,
    "butter": 102,
    "olive oil (1 tbsp)": 119,
    "rice cake": 35,
    "popcorn (1 cup)": 55,
}

print("Avialable food items:" ) 
for food in food_data:
   print("-",food) 

while True:
   item=input(("Enter food item:").lower())
   if item=="done":
      break
   
   if item in food_data:
      total_calories += food_data[item]
      print(f"Added {item} ({food_data[item]} calories).")
   else:
      print("Food not found! try again")


print("\n Total Calories Eaten Today:",total_calories)


print("Suggestion:", cal_suggestion(total_calories))

    