servings = int(input("How many servings would you like? "))

oil = 60*servings
chili = 0.5*servings
garlic = 3*servings
parsley = 8*servings
linguine = 125*servings

print("PASTA AGLIO E OLIO")
print("------------------")
print(f"Ingredients ({servings} serving(s)):")
print(f"* Extra virgin olive oil: {oil} ml")
print(f"* Chili flakes: {chili} tsp")
print(f"* Garlic: {garlic} cloves")
print(f"* Flat-leaf parsley: {parsley} g")
print(f"* Linguine: {linguine} g")