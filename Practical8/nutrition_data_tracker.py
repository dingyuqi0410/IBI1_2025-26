class food_item(object):
    def __init__(self,name,calories,protein,carbohydrates,fat):
        self.name=name
        self.calories=calories
        self.protein=protein
        self.carbohydrates=carbohydrates
        self.fat=fat
def track_nutrition(consumed_items):     
    total_calories=0
    total_protein=0
    total_carbohydrates=0
    total_fat=0
    for item in consumed_items:
        total_calories+=item.calories
        total_protein+=item.protein
        total_carbohydrates+=item.carbohydrates
        total_fat+=item.fat
    print(f"Total calories: {total_calories}")
    print(f"Total protein: {total_protein} g")
    print(f"Total carbohydrates: {total_carbohydrates} g")
    print(f"Total fat: {total_fat} g")
    if total_calories>2500:
        print("Warning: calories intake is above 2500 calories.")
    if total_fat>90:    
        print("Warning: fat intake is above 90 g.")
    return total_calories,total_protein,total_carbohydrates,total_fat    
burger=food_item("Burger",800,35,50,45)
pizza=food_item("Pizza",900,30,80,30)
milkshake=food_item("Milkshake",450,10,60,15)
ice_cream=food_item("Ice cream",400,5,45,20)
foods_today=[burger,pizza,milkshake,ice_cream]
totals=track_nutrition(foods_today)     
print(f"Returned totals: {totals}")      