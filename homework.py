class Recipe:
    def __init__(self, name, ingredients, instructions):
        """Initialize the recipe with a name, list of ingredients, and preparation instructions."""
        self.name = name
        self.ingredients = ingredients  # List of ingredients
        self.instructions = instructions  # List of preparation steps
        self._index = 0  # For iteration

    def __str__(self):
        """Return a string representation of the recipe."""
        ingredients_list = "\n".join(f"- {ing}" for ing in self.ingredients)
        instructions_list = "\n".join(f"{i+1}. {step}" for i, step in enumerate(self.instructions))
        return f"📌 Recipe: {self.name}\n\n🛒 Ingredients:\n{ingredients_list}\n\n👨‍🍳 Instructions:\n{instructions_list}"

# Creating 3 recipes
recipe1 = Recipe(
    "Pancakes",
    ["Flour", "Milk", "Eggs", "Sugar", "Butter"],
    [
        "Mix all ingredients together in a bowl.",
        "Heat a pan over medium heat.",
        "Pour batter into the pan and cook until bubbles appear.",
        "Flip and cook the other side until golden brown.",
        "Serve with syrup or toppings of choice."
    ]
)

recipe2 = Recipe(
    "Spaghetti Bolognese",
    ["Spaghetti", "Ground Beef", "Tomato Sauce", "Garlic", "Onion", "Olive Oil"],
    [
        "Boil water and cook spaghetti according to package instructions.",
        "Chop the onion and garlic.",
        "Heat olive oil in a pan and sauté onion and garlic until soft.",
        "Add ground beef and cook until browned.",
        "Pour in tomato sauce and simmer for 15 minutes.",
        "Serve the sauce over the spaghetti."
    ]
)

recipe3 = Recipe(
    "Greek Salad",
    ["Tomatoes", "Cucumber", "Feta Cheese", "Olives", "Olive Oil"],
    [
        "Chop tomatoes and cucumber into small pieces.",
        "Cut feta cheese into cubes.",
        "Combine all ingredients in a bowl.",
        "Drizzle with olive oil and mix gently.",
        "Serve fresh and enjoy!"
    ]
)

# Printing the recipes
print(recipe1)
print("\n" + "="*50 + "\n")
print(recipe2)
print("\n" + "="*50 + "\n")
print(recipe3)

'''
# Using iterator to loop through ingredients
print("\n🛒 Ingredients in Pancakes Recipe:")
for ingredient in recipe1:
    print(ingredient)

# Using index to access a specific ingredient
print("\n🔎 First ingredient in Pancakes:", recipe1[0])
print("🔎 Third ingredient in Greek Salad:", recipe3[2])
'''