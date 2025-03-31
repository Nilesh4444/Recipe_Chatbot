from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Updated Recipe Database
recipes = [
    {
        "name": "Pasta",
        "ingredients": ["tomato", "pasta", "cheese", "olive oil", "garlic"],
        "cuisine": "Italian",
        "diet": "Vegetarian",
        "steps": [
            "Boil water in a pot and add pasta. Cook for 8-10 minutes until al dente.",
            "Heat olive oil in a pan, sauté garlic, and add tomato sauce.",
            "Mix the cooked pasta with the sauce and stir well.",
            "Sprinkle cheese on top and serve hot."
        ]
    },
    {
        "name": "Chicken Curry",
        "ingredients": ["chicken", "onion", "spices", "tomato", "garlic", "ginger"],
        "cuisine": "Indian",
        "diet": "Non-Vegetarian",
        "steps": [
            "Heat oil in a pan and sauté onions until golden brown.",
            "Add chopped tomatoes, garlic, ginger, and spices, then cook for 5 minutes.",
            "Add chicken pieces and cook until browned.",
            "Pour in water, cover, and let it simmer for 20 minutes until fully cooked.",
            "Garnish with fresh coriander and serve with rice or naan."
        ]
    },
    {
        "name": "Vegetable Stir Fry",
        "ingredients": ["broccoli", "carrot", "bell pepper", "soy sauce", "garlic"],
        "cuisine": "Chinese",
        "diet": "Vegetarian",
        "steps": [
            "Chop all vegetables into bite-sized pieces.",
            "Heat oil in a wok and add garlic.",
            "Stir-fry vegetables for 5-7 minutes until slightly tender.",
            "Add soy sauce and stir for another 2 minutes.",
            "Serve hot with rice or noodles."
        ]
    }
]

@app.route("/search", methods=["GET"])
def search_recipe():
    ingredient = request.args.get("ingredient", "").lower()
    cuisine = request.args.get("cuisine", "").lower()
    diet = request.args.get("diet", "").lower()

    matching_recipes = [
        r for r in recipes
        if (not ingredient or any(ingredient in i for i in r["ingredients"]))
        and (not cuisine or cuisine == r["cuisine"].lower())
        and (not diet or diet == r["diet"].lower())
    ]

    if not matching_recipes:
        return jsonify({"error": "No recipes found! Please check your input."}), 404

    return jsonify(matching_recipes)

if __name__ == "__main__":
    app.run(debug=True)
