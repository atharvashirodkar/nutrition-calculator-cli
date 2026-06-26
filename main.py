from database.db import init_db
from menu import menu
from modules.calculator import calculate_nutrition
from modules.validator import validate_weight
from modules.report_service import (
    create_report,
    delete_report,
    get_all_reports,
    get_report_by_id,
)
from modules.csv_exporter import export_reports_to_csv
from modules.formatter import (
    format_nutrition_report,
    format_report_with_weights,
    report_to_dict,
)


def main():
    while True:
        menu()
        option = input("Choose Option: ").strip()

        match option:
            case "1":
                try:
                    current_body_weight = float(
                        input("Enter your current body weight (kg): ")
                    )
                    goal_body_weight = float(
                        input("Enter your goal body weight (kg): ")
                    )

                    validate_weight(current_body_weight, "Current Body weight")
                    validate_weight(goal_body_weight, "Goal body weight")

                    print(f"\nCurrent Weight (kg): {current_body_weight}")
                    print(f"Goal Weight (kg): {goal_body_weight}")

                    nutrition = calculate_nutrition(
                        current_body_weight, goal_body_weight
                    )  # return dict

                    print(format_nutrition_report(nutrition))

                    post_data = {
                        "current_weight": current_body_weight,
                        "goal_weight": goal_body_weight,
                        **nutrition,
                    }

                    create_report(post_data)

                except ValueError as e:
                    print(f"Error: {e}")

            case "2":
                reports = get_all_reports()
                if not reports:
                    print("No reports found.")
                else:
                    for report in reports:
                        print(format_report_with_weights(report_to_dict(report)))

            case "3":
                try:
                    report_id = int(input("Enter the report id: "))

                    report = get_report_by_id(report_id)

                    if report:
                        print(format_report_with_weights(report_to_dict(report)))
                    else:
                        print("Report not found.")
                except ValueError:
                    print("Error: Invalid Report ID")

            case "4":
                try:
                    report_id = int(input("Enter the report id to delete report: "))
                    confirmation = (
                        input("Do you really want to delete the report? (y/n): ")
                        .strip()
                        .lower()
                    )

                    if confirmation in ("y", "yes"):
                        if delete_report(report_id):
                            print("Report deleted.")
                        else:
                            print("Report not found.")
                    else:
                        print("Deletion cancelled.")
                except ValueError as e:
                    print("Error: Invalid Report ID")

            case "5":
                reports = get_all_reports()
                if reports:
                    export_reports_to_csv(reports)
                    print("Reports exported successfully.")
                else:
                    print("No reports to export.")

            case "6":
                print("Exiting Program...")
                break
            case _:
                print("Invalid input")


if __name__ == "__main__":
    init_db()  # Initialize the database and create tables if they don't exist
    main()
