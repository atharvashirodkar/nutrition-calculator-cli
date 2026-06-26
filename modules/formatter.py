def format_nutrition_report(data):

    report = (
        "\nDaily Nutrition Targets\n"
        "------------------------------------\n"
        f'Calories       : {data["calories"]} kcal\n'
        f'Protein        : {data["protein"]} g\n'
        f'Fat            : {data["fat"]} g\n'
        f'Fiber          : {data["fiber"]} g\n'
        f'Carbohydrates  : {data["carbohydrates"]:.2f} g\n'
        "------------------------------------"
    )
    return report

def format_report_with_weights(data):
    report = (
        "\nWeight & Daily Nutrition Report\n"
        "====================================\n"
        f'ID #{data["id"]} | Created: {data["created_at"].strftime("%d %b %Y")}\n'
        "------------------------------------\n"
        f'Current Weight : {data["current_weight"]:.2f} kg\n'
        f'Goal Weight    : {data["goal_weight"]:.2f} kg\n'
        "------------------------------------\n"
        f'Calories       : {data["calories"]:.0f} kcal\n'
        f'Protein        : {data["protein"]:.2f} g\n'
        f'Fat            : {data["fat"]:.2f} g\n'
        f'Fiber          : {data["fiber"]:.2f} g\n'
        f'Carbohydrates  : {data["carbohydrates"]:.2f} g\n'
        "===================================="
    )

    return report

def report_to_dict(report):
    return {
        "id": report.id,
        "current_weight": report.current_weight,
        "goal_weight": report.goal_weight,
        "calories": report.calories,
        "protein": report.protein,
        "fat": report.fat,
        "fiber": report.fiber,
        "carbohydrates": report.carbohydrates,
        "created_at": report.created_at,
    }