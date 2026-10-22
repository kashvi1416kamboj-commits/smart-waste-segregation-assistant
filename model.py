import ollama

WASTE_RULES = {
    "plastic": {
        "category": "Dry / Recyclable Waste",
        "guidance": (
            "Keep plastic separate from wet waste and "
            "hand it over through the appropriate local "
            "collection or recycling system."
        )
    },
    "paper": {
        "category": "Dry / Recyclable Waste",
        "guidance": (
            "Keep paper dry and separate from wet waste "
            "for recycling."
        )
    },
    "food": {
        "category": "Wet / Biodegradable Waste",
        "guidance": (
            "Keep food waste separate from dry waste "
            "and follow the local wet-waste collection system."
        )
    },
    "battery": {
        "category": "Special / Hazardous Waste",
        "guidance": (
            "Do not mix used batteries with ordinary "
            "household waste. Use an appropriate battery "
            "collection or recycling channel."
        )
    },
    "electronics": {
        "category": "E-Waste",
        "guidance": (
            "Do not mix electronic waste with ordinary "
            "household waste. Use an appropriate e-waste "
            "collection or recycling channel."
        )
    }
}
def waste_analyzer(image_bytes):
 
    prompt = """
You are an AI Smart Waste Segregation Assistant.
Carefully examine the uploaded image and identify the object as accurately
as possible.

Your job is not only to name the object. You must explain the object,
its material, waste classification, environmental impact, reuse options,
recycling possibilities and correct disposal method.

Give a detailed answer using the following format.
1. PRODUCT IDENTIFICATION

Product / Item:
Give the exact name of the object if possible.

What is it?
Explain what the product is and what it is normally used for.

What do you see in the image?
Describe the visible features that helped you identify the object.

Identification Reason:
Explain why you believe the object is this particular product.

If you are not completely certain, clearly mention the uncertainty.
2. MATERIAL ANALYSIS

Main Material:
Identify the most likely material.

Possible Materials:
Mention other materials that could be present.

Material Properties:
Briefly explain whether the material is flexible, rigid, lightweight,
durable, waterproof, biodegradable, etc.

Do not claim an exact material if it cannot be determined from the image.
Use words such as "likely" when necessary.

3. WASTE CLASSIFICATION

Waste Category:
Choose the most appropriate category:
- Wet Waste
- Dry Waste
- Plastic Waste
- Paper Waste
- Metal Waste
- Glass Waste
- E-Waste
- Hazardous Waste
- Textile Waste
- Other
Explain why the item belongs to this category.

Important:
Classify the actual object shown in the image, not just a related product.

4. RECYCLABILITY

Is it recyclable?
Answer Yes, No, or Depends.
Explain why.
What part can be recycled?
Mention the material or component that may be recyclable.
Recycling Difficulty:
Mention if recycling this item is easy, difficult or material-dependent.

5. DECOMPOSITION

Estimated Decomposition Time:
Give an approximate time period for the material to break down.
Explain:
Why does it take this long?
Mention that decomposition depends on environmental conditions
such as sunlight, moisture, temperature and landfill conditions.

Do not give a false exact number if the material is uncertain.

6. REUSE POSSIBILITIES
Give at least 3 practical ways the item could be reused.
Reuse Idea 1:
Explain it.

Reuse Idea 2:
Explain it.

Reuse Idea 3:
Explain it.

Also mention whether the item can be repaired, donated or repurposed.

7. ENVIRONMENTAL IMPACT

Explain the environmental impact of this type of waste.
Discuss relevant points such as:
- Pollution
- Landfill waste
- Microplastics
- Soil contamination
- Water pollution
- Air pollution
- Greenhouse gases
- Resource consumption
- Harm to animals
Only mention impacts that are relevant to this particular item.

8. DISPOSAL GUIDANCE

What should the user do with this item?
Give clear step-by-step disposal guidance.
Step 1:
What should the user do first?
Step 2:
How should it be separated?
Step 3:
Where should it ideally go?
Mention recycling, collection centres or special waste facilities
when appropriate.
Also mention if it should NOT be placed in normal household waste.

9. BETTER ENVIRONMENTAL CHOICE

Give practical suggestions for reducing waste from this product.
Examples:
- Reuse
- Repair
- Donate
- Buy durable products
- Avoid unnecessary replacement
- Choose recyclable materials
- Choose reusable alternatives

10. GEEKY FACT

Give 2 or 3 interesting facts about the product or its material.
The facts should be useful and related to waste management,
materials or environmental science.

 11. QUICK SUMMARY

At the end give a short summary:
Product:
Material:
Waste Type:
Recyclable:
Decomposition:
Best Disposal Method:
Best Reuse Option:

Keep the explanation detailed but easy to understand.
Do not invent information that cannot be determined from the image.
Clearly distinguish between confirmed observations and likely assumptions.
"""
    response = ollama.chat(
        model="moondream",
        messages=[
            {
                "role":"user",
                "content": prompt,
                "images":[image_bytes]
            }
        ]
    )
    identification= response["message"]["content"] 
    text = identification.lower()

    if "battery" in text:
        rule = WASTE_RULES["battery"]
    elif any(word in text for word in [
        "electronic device",
        "charger",
        "laptop",
        "computer",
        "keyboard",
        "mouse"
    ]):
        rule = WASTE_RULES["electronics"]
    elif any(word in text for word in [
        "plastic",
        "bottle",
        "wrapper",
        "polythene",
        "plastic bag"
    ]):
        rule = WASTE_RULES["plastic"]
    elif any(word in text for word in [
        "paper",
        "cardboard",
        "newspaper"
    ]):
        rule = WASTE_RULES["paper"]
    elif any(word in text for word in [
        "food",
        "fruit",
        "vegetable",
        "vegetables",
        "food waste"
    ]):
        rule = WASTE_RULES["food"]
    else:
        rule = {
            "category": "Other / Needs Local Guidance",
            "guidance": (
                "Keep the item separate until its material "
                "and appropriate disposal method can be confirmed."
            )
        }
    result= f"""

{identification}

### ♻️Waste Category

{rule["category"]}

### 🗑️Disposal Guidance
{rule["guidance"]}

### ⚠️ Important

This is general waste-management guidance.
Local municipal collection and recycling arrangements
may differ.
"""
    return result