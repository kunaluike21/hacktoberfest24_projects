from flask import Flask, request, jsonify

app = Flask(__name__)

recipes = [
    {"name": "Butter Chicken", "ingredients": ["chicken", "butter", "cream", "tomatoes", "spices"]},
    {"name": "Paneer Tikka", "ingredients": ["paneer", "yogurt", "spices"]},
    {"name": "Biryani", "ingredients": ["rice", "chicken", "yogurt", "spices"]},
    {"name": "Chole Bhature", "ingredients": ["chickpeas", "flour", "spices"]},
    {"name": "Dosa", "ingredients": ["rice", "lentils"]},
    {"name": "Palak Paneer", "ingredients": ["spinach", "paneer", "cream", "spices"]},
    {"name": "Rajma", "ingredients": ["kidney beans", "tomatoes", "spices"]},
    {"name": "Aloo Paratha", "ingredients": ["potato", "flour", "spices"]},
    {"name": "Tandoori Chicken", "ingredients": ["chicken", "yogurt", "spices"]},
    {"name": "Masala Dosa", "ingredients": ["rice", "lentils", "potato", "spices"]},
    {"name": "Pav Bhaji", "ingredients": ["bread", "mixed vegetables", "spices"]},
    {"name": "Vada Pav", "ingredients": ["potato", "bread", "spices"]},
    {"name": "Samosa", "ingredients": ["potato", "flour", "spices"]},
    {"name": "Rogan Josh", "ingredients": ["mutton", "yogurt", "spices"]},
    {"name": "Paneer Butter Masala", "ingredients": ["paneer", "butter", "cream", "tomatoes", "spices"]},
    {"name": "Gulab Jamun", "ingredients": ["milk solids", "flour", "sugar syrup"]},
    {"name": "Jalebi", "ingredients": ["flour", "sugar syrup"]},
    {"name": "Kheer", "ingredients": ["milk", "rice", "sugar"]},
    {"name": "Pani Puri", "ingredients": ["flour", "tamarind water", "potato", "chickpeas"]},
    {"name": "Dhokla", "ingredients": ["gram flour", "yogurt", "spices"]},
    {"name": "Pulao", "ingredients": ["rice", "vegetables", "spices"]},
    {"name": "Rasam", "ingredients": ["tamarind", "tomatoes", "spices"]},
    {"name": "Upma", "ingredients": ["semolina", "vegetables", "spices"]},
    {"name": "Idli", "ingredients": ["rice", "lentils"]},
    {"name": "Sambar", "ingredients": ["lentils", "vegetables", "spices"]},
    {"name": "Korma", "ingredients": ["meat", "yogurt", "spices"]},
    {"name": "Bhindi Masala", "ingredients": ["okra", "tomatoes", "spices"]},
    {"name": "Chicken Tikka", "ingredients": ["chicken", "yogurt", "spices"]},
    {"name": "Lassi", "ingredients": ["yogurt", "sugar", "spices"]},
    {"name": "Naan", "ingredients": ["flour", "yeast", "milk"]},
    {"name": "Malai Kofta", "ingredients": ["paneer", "potato", "cream", "spices"]},
    {"name": "Aloo Gobi", "ingredients": ["potato", "cauliflower", "spices"]},
    {"name": "Baingan Bharta", "ingredients": ["eggplant", "tomatoes", "spices"]},
    {"name": "Matar Paneer", "ingredients": ["peas", "paneer", "tomatoes", "spices"]},
    {"name": "Fish Curry", "ingredients": ["fish", "coconut milk", "spices"]},
    {"name": "Raita", "ingredients": ["yogurt", "cucumber", "spices"]},
    {"name": "Khichdi", "ingredients": ["rice", "lentils", "vegetables", "spices"]},
    {"name": "Sev Puri", "ingredients": ["flour", "potato", "tamarind", "spices"]},
    {"name": "Dal Makhani", "ingredients": ["lentils", "butter", "cream", "spices"]},
    {"name": "Kati Roll", "ingredients": ["bread", "meat or vegetables", "spices"]},
    {"name": "Papdi Chaat", "ingredients": ["flour", "potato", "yogurt", "chickpeas"]},
    {"name": "Mango Chutney", "ingredients": ["mango", "sugar", "spices"]},
    {"name": "Pesarattu", "ingredients": ["green gram", "rice"]},
    {"name": "Nimbu Pani", "ingredients": ["lemon", "sugar", "water"]},
    {"name": "Kadhi", "ingredients": ["yogurt", "gram flour", "spices"]},
    {"name": "Shahi Paneer", "ingredients": ["paneer", "cream", "tomatoes", "spices"]},
    {"name": "Poori", "ingredients": ["flour", "oil"]},
    {"name": "Saag", "ingredients": ["mustard greens", "spinach", "spices"]},
]

@app.route('/recipes', methods=['GET', 'POST'])
def manage_recipes():
    if request.method == 'POST':
        recipe = request.json
        recipes.append(recipe)
        return jsonify(recipe), 201
    else:
        return jsonify(recipes)

if __name__ == '__main__':
    app.run(debug=True)
