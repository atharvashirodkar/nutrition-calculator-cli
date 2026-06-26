# 🏋️ Nutrition Calculator CLI

## 📖 Project Overview

Nutrition Calculator CLI is a Python command-line application that helps users estimate their daily calorie and macronutrient requirements based on body weight and fitness goals. The application uses current body weight and goal body weight to calculate recommended calorie, protein, fat, fiber, and carbohydrate targets based on predefined formulas. It provides a convenient way to generate personalized nutrition goals while operating entirely offline without relying on third-party services.

## 🎯 Project Objectives

The primary objective of this project is to help users understand their daily calorie and macronutrient requirements while practicing fundamental Python programming concepts. The application focuses on calculation logic, user input handling, data validation, database operations, and structured program design.

## ✨ Features

- Calculate daily calorie requirements based on body weight and fitness goals.
- Calculate daily protein requirements based on goal body weight.
- Calculate daily fat requirements for hormone support.
- Calculate daily fiber requirements for digestive health.
- Calculate daily carbohydrate requirements using remaining calories.
- Display a complete daily nutrition summary.
- Validate user input to prevent invalid calculations.
- Save nutrition calculations to a SQLite database.
- View previous nutrition reports.
- Search calculation history by date.
- Delete saved reports when no longer needed.
- Export nutrition reports to CSV format for analysis and backup.
  
## 🧮 Calculation Formula

### Daily Calories

```text
Daily Calories = Current Body Weight × 40
```

### Daily Protein

```text
Protein (g) = Goal Body Weight × 1.5
```

### Daily Fat

```text
Fat (g) = Current Body Weight × 0.8
```

### Daily Fiber

```text
Fiber (g) = Current Body Weight × 0.7
```

### Daily Carbohydrates

```text
Remaining Calories =
Total Calories -
(Protein × 4) -
(Fat × 9)

Carbohydrates (g) =
Remaining Calories ÷ 4
```

## 📊 Example Calculation

### User Input

```text
Current Weight: 60 kg
Goal Weight: 70 kg
```

### Results

```text
Calories: 2400 kcal
Protein: 105 g
Fat: 48 g
Fiber: 42 g
Carbohydrates: 365.75 g
```

## 🔄 User Flow

1. Launch the application.
2. Enter current body weight.
3. Enter goal body weight.
4. System validates the entered values.
5. Application performs all nutrition calculations.
6. Results are displayed in a formatted report.
7. Results are stored in the SQLite database.
8. User can view, search, delete, or export reports.
9. User may perform another calculation or exit.

## 📁 Project Structure

```text
nutrition-calculator-cli/
├── database/
│   ├── db.py
│   └── models.py
├── modules/
│   ├── calculator.py
│   ├── validator.py
│   ├── formatter.py
│   ├── report_service.py
│   └── csv_exporter.py
├── utils/
│   └── constants.py
├── nutrition.db
├── main.py
├── requirements.txt
└── README.md
```

## 🗄️ Database Schema

### nutrition_reports

| Column | Type |
|----------|----------|
| id | Integer |
| current_weight | Float |
| goal_weight | Float |
| calories | Float |
| protein | Float |
| fat | Float |
| fiber | Float |
| carbohydrates | Float |
| created_at | DateTime |

Each completed calculation is stored as a nutrition report, allowing users to review historical data and track changes over time.

## 🏗️ Core Modules

### calculator.py

Contains all nutrition calculation formulas and business logic.

### validator.py

Handles validation for body weight and goal weight inputs.

### formatter.py

Formats calculation results into a clean console report.

### report_service.py

Handles creation, retrieval, search, and deletion of nutrition reports.

### csv_exporter.py

Exports nutrition reports to CSV format for analysis and backup.

### database/db.py

Creates the SQLAlchemy engine, session, and database connection.

### database/models.py

Defines database tables and ORM models used by the application.


## 🐍 Python Concepts Covered

| Concept | Purpose |
|----------|----------|
| Variables | Store user inputs and calculation results |
| Functions | Separate calculation logic into reusable units |
| Conditional Statements | Validate user inputs |
| Loops | Allow multiple calculations in a single session |
| Modules | Organize project structure |
| SQLite | Persistent data storage |
| SQLAlchemy ORM | Database interaction through Python objects |
| CRUD Operations | Create, Read, Update, Delete nutrition reports |
| CSV Handling | Export reports for analysis |
| Exception Handling | Prevent application crashes from invalid input |
| Database Design | Work with tables, columns, and records |


## 💻 Sample CLI Output

```text
====================================
 Nutrition Calculator
====================================

1. New Calculation
2. View Reports
3. Search Reports
4. Delete Report
5. Export Reports to CSV
6. Exit

Choose Option: 1

Current Weight (kg): 60
Goal Weight (kg): 70

Daily Nutrition Targets
------------------------------------
Calories       : 2400 kcal
Protein        : 105 g
Fat            : 48 g
Fiber          : 42 g
Carbohydrates  : 365.75 g
------------------------------------

Report saved successfully.
```

## 🚀 Future Enhancements

- BMI calculator.
- Maintenance calorie calculator.
- Weight gain mode.
- Weight loss mode.
- Weight maintenance mode.
- Activity level adjustments.
- Meal planning suggestions.
- Progress tracking system.
- Weekly nutrition reports.
- Multi-user support.

## 🎓 Learning Outcomes

By completing this project, learners will gain practical experience in implementing mathematical formulas, validating user input, structuring Python applications, designing database models with SQLAlchemy ORM, performing CRUD operations with SQLite, exporting data to CSV, and building command-line software that stores and manages real-world data.