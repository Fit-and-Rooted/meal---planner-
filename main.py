import streamlit as st
import random

# ----------------------------- #
#       MEAL DATABASE SETUP     #
# ----------------------------- #

# 🥣 Breakfast options
breakfasts = [
    {"name": "Crispy feta eggs", "calories": 500, "protein": 25},
    {"name": "Chia berry compote granolla", "calories": 210, "protein": 9},
    {"name": "Prepable Breakfast muffins", "calories": 287, "protein": 22},
    {"name": "Hot honey halloumi avocado toast", "calories": 450, "protein": 22},
    {"name": "Smoked salmon and cream cheese omelette", "calories": 300, "protein": 26},
    {"name": "Lighter sausage breakfast bagels", "calories": 450, "protein": 24},
    {"name": "Breakfast banana bread loaf (pg 16)", "calories": 250, "protein": 4},
    {"name": "Chocolate Orange oats with Citrus Honey (pg15)", "calories": 350, "protein": 15}
]

# 🥗 Lunch options
lunches = [
    {"name": "Mango, Jalapeno and Lime salad (pg 42)", "calories": 450, "protein": 23},
    {"name": "Crunchy Peanut slaw (pg 49)", "calories": 250, "protein": 9},
    {"name": "Toasted sesame and ginger chicken salad", "calories": 500, "protein": 56},
    {"name": "Speedy chicken and spicy guacamole tacos (pg52)", "calories": 450, "protein": 20},
    {"name": "Nature's multivitamin", "calories": 300, "protein": 9},
    {"name": "Best ever caesar Salad", "calories": 400, "protein": 30},
    {"name": "Lighter pesto pasta salad", "calories": 350, "protein": 15},
    {"name": "Sushi salad", "calories": 450, "protein": 15},
    {"name": "The glow bowl", "calories": 400, "protein": 20},
    {"name": "The I-have-no-time tuna salad", "calories": 300, "protein": 28},
    {"name": "Oven baked feta and pepper pasta", "calories": 450, "protein": 15},
    {"name": "Skin glow omega bowl", "calories": 350, "protein": 17},
    {"name": "Sticky honey halloumi salad", "calories": 400, "protein": 20}
]

# 🧃 Snack options
snacks = [
    {"name": "Skin glow crackers and caramelised onion hummus", "calories": 254, "protein": 9},
    {"name": "Smacked cucumbers", "calories": 50, "protein": 5},
    {"name": "Lighter hummus and veggie sticks", "calories": 150, "protein": 10},
    {"name": "Dark chocolate roasted almond bites", "calories": 70, "protein": 2},
    {"name": "Naked bars", "calories": 113, "protein": 2.3}
]

# 🍽 Dinner options
dinner = [
    {"name": "Butternut squash mac and cheese", "calories": 500, "protein": 21},
    {"name": "Prawn and sriracha burgers", "calories": 400, "protein": 22},
    {"name": "Pesto prawn courgetti linguini", "calories": 400, "protein": 26},
    {"name": "Brick almond chicken with honey and lime slaw", "calories": 350, "protein": 35},
    {"name": "Tarragon Lasagne", "calories": 400, "protein": 22},
    {"name": "Garlic crumbled salmon with courgettes and yogurt", "calories": 600, "protein": 50},
    {"name": "Tuna Puttanesca Spaghetti", "calories": 350, "protein": 28},
    {"name": "Sticky peanut stir fry", "calories": 500, "protein": 30},
    {"name": "One pan Tuscan salmon", "calories": 500, "protein": 38},
    {"name": "Salmon and sexy veg", "calories": 126, "protein": 22},
    {"name": "Spinach and ricotta malfatti", "calories": 400, "protein": 20},
    {"name": "Chicken katsu curry", "calories": 550, "protein": 30},
    {"name": "Chicken and smoky romesco", "calories": 500, "protein": 20},
    {"name": "Wholegrain fish and chips", "calories": 500, "protein": 33},
    {"name": "Italian sausage and broccoli pasta", "calories": 632, "protein": 40},
    {"name": "Spiced turkey koftas with tabbouleh and mint yogurt", "calories": 400, "protein": 47},
    {"name": "Hot and sour Thai bowl", "calories": 400, "protein": 10}
]

# ----------------------------- #
#         STREAMLIT UI          #
# ----------------------------- #

st.title("🌞 7-Day Meal Planner")
st.write("Tailor a full week of meals to your daily calorie goal and protein needs.")

target = st.number_input("Enter your daily calorie target:", min_value=800, max_value=4000, value=1800, step=100)

if st.button("Generate Plan"):
    st.subheader("📅 Your Weekly Meal Plan")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for day in days:
        breakfast = random.choice(breakfasts)
        lunch = random.choice(lunches)
        dinner_choice = random.choice(dinner)
        snack = random.choice(snacks)

        total_calories = breakfast["calories"] + lunch["calories"] + dinner_choice["calories"] + snack["calories"]
        total_protein = breakfast["protein"] + lunch["protein"] + dinner_choice["protein"] + snack["protein"]
        difference = total_calories - target

        st.markdown(f"**{day}:**")
        st.write(f"🍳 Breakfast: {breakfast['name']} ({breakfast['calories']} cal, {breakfast['protein']}g protein)")
        st.write(f"🥗 Lunch: {lunch['name']} ({lunch['calories']} cal, {lunch['protein']}g protein)")
        st.write(f"🍽️ Dinner: {dinner_choice['name']} ({dinner_choice['calories']} cal, {dinner_choice['protein']}g protein)")
        st.write(f"🥒 Snack: {snack['name']} ({snack['calories']} cal, {snack['protein']}g protein)")
        st.write(f"💪 Total: {total_calories} calories, {round(total_protein,1)}g protein")
        st.caption(f"🔍 This is {abs(difference)} calories {'above' if difference > 0 else 'below'} your target of {target}.")

    st.success("Done! Your complete 7-day plan is ready to go.")
