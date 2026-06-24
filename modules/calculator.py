def calculate_calories(current_body_weight):
    return current_body_weight * 40


def calculate_protein(goal_body_weight):
    return goal_body_weight * 1.5


def calculate_fat(current_body_weight):
    return current_body_weight * 0.8


def calculate_fiber(current_body_weight):
    return current_body_weight * 0.7


def calculate_carbohydrates(total_calories, protein, fat):
    remaining_calories = total_calories - (protein * 4) - (fat * 9)
    carbohydrates = remaining_calories / 4
    return carbohydrates


def calculate_nutrition(current_body_weight, goal_body_weight):
    calories = calculate_calories(current_body_weight)
    protein = calculate_protein(goal_body_weight)
    fat = calculate_fat(current_body_weight)
    fiber = calculate_fiber(current_body_weight)
    carbohydrates = calculate_carbohydrates(calories, protein, fat)
    return {
        "calories": calories,
        "protein": protein,
        "fat": fat,
        "fiber": fiber,
        "carbohydrates": carbohydrates,
    }
