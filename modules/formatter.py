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
