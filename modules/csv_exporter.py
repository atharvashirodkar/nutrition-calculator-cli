import csv


def export_reports_to_csv(reports):
    result = [
        [
            r.id,
            r.current_weight,
            r.goal_weight,
            r.calories,
            r.protein,
            r.fat,
            r.fiber,
            r.carbohydrates,
            r.created_at,
        ]
        for r in reports
    ]
    header = [
        "id",
        "current_weight",
        "goal_weight",
        "calories",
        "protein",
        "fat",
        "fiber",
        "carbohydrates",
        "created_at",
    ]
    with open("nutrition_reports.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(result)
