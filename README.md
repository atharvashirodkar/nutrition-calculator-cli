# 🏋️ Nutrition Calculator CLI

A lightweight Python command-line application that calculates personalized daily calorie and macronutrient requirements based on body weight and fitness goals.

## 📘 Project Overview

**Nutrition Calculator CLI** is an offline-first CLI tool designed to help users quickly estimate their daily nutrition targets without external dependencies. By entering just two values—current body weight and goal body weight—the application calculates optimal daily intake for:

- 🔥 **Calories** – energy expenditure estimation
- 💪 **Protein** – muscle recovery and growth
- 🥑 **Fat** – hormone support and nutrient absorption
- 🥕 **Fiber** – digestive health
- 🍚 **Carbohydrates** – primary energy source

All calculations are stored in a local SQLite database, enabling users to track nutrition goals over time, search historical reports, and export data to CSV.

## 💡 Why It Matters

### For Users
- **Personalized Goals** – Get nutrition targets tailored to your current and goal weight
- **Offline & Private** – All data stays on your machine; no cloud dependencies or data sharing
- **Quick & Simple** – Calculate your macros in seconds with just two inputs
- **Track Progress** – Save and review past calculations to monitor your fitness journey
- **Export & Analyze** – Extract reports to CSV for spreadsheet analysis or sharing

### For Developers
This project is an excellent learning resource for:
- **Python Fundamentals** – Input validation, loops, and data structures
- **CLI Development** – Building user-friendly command-line interfaces
- **Database Operations** – SQLAlchemy ORM, SQLite, and CRUD operations
- **Code Organization** – Modular design with separation of concerns
- **Testing Scenarios** – Real-world calculations and edge cases

## ⚙️ Getting Started

### Prerequisites
- **Python 3.8+**
- **pip** (Python package manager)

### Installation

1. **Clone or Download** the project:
   ```bash
   git clone https://github.com/atharvashirodkar/nutrition-calculator-cli.git
   ```

2. **Create a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - **Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **Windows (Command Prompt):**
     ```cmd
     .\venv\Scripts\activate.bat
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**:
   ```bash
   python main.py
   ```

### Usage

Run the application:
```bash
python main.py
```

#### Menu Options

```
====================================
Nutrition Calculator
====================================
1. New Calculation      – Calculate macronutrient targets for custom weights
2. View Reports         – Browse all saved nutrition calculations
3. Search Report        – Find reports by specific id 
4. Delete Report        – Remove unwanted entries from history
5. Export Reports to CSV – Export all reports for external analysis
6. Exit                 – Close the application
```

#### Example Workflow

```bash
$ python main.py

====================================
Nutrition Calculator
====================================
1. New Calculation
2. View Reports
3. Search Report
4. Delete Report
5. Export Reports to CSV
6. Exit

Choose Option: 1
Enter your current body weight (kg): 60
Enter your goal body weight (kg): 70

Current Weight (kg): 60.0
Goal Weight (kg): 70.0

Daily Nutrition Targets
--------------------------------
Calories:      2400 kcal
Protein:       105.00 g
Fat:           48.00 g
Fiber:         42.00 g
Carbs:         365.75 g
```

### Calculation Formulas

The application uses simple formulas for estimating nutrition targets:

| Nutrient | Formula | Purpose |
|----------|---------|---------|
| **Calories** | Current Weight × 40 | Daily energy expenditure |
| **Protein** | Goal Weight × 1.5 | Muscle growth & recovery |
| **Fat** | Current Weight × 0.8 | Hormone production |
| **Fiber** | Current Weight × 0.7 | Digestive health |
| **Carbs** | (Calories - (Protein × 4) - (Fat × 9)) ÷ 4 | Remaining energy source |

## 🛠️ Tech Stack

- Python 3
- SQLite
- SQLAlchemy ORM
- CSV
- Layered Architecture (Service Layer Pattern)

## 📂 Project Structure

```
nutrition-calculator-cli/
├── database/
│   ├── __init__.py
│   ├── db.py                # SQLite database setup & session management
│   └── models.py            # SQLAlchemy ORM model for nutrition reports
├── modules/
│   ├── __init__.py
│   ├── calculator.py        # Core nutrition calculation logic
│   ├── csv_exporter.py      # CSV export functionality
│   ├── formatter.py         # Report formatting & display helpers
│   ├── report_service.py    # Database CRUD operations
│   └── validator.py         # Input validation & error handling
├── main.py                  # Application entry point & menu loop
├── menu.py                  # CLI menu display
├── overview.md              # Project documentation
├── README.md                # This file
└── nutrition.db             # SQLite database (auto-generated)
```

## ✨ Features

- Daily calorie and macronutrient calculation
- Input validation
- SQLite database storage
- SQLAlchemy ORM integration
- View saved reports
- Search reports by ID
- Delete reports
- Export reports to CSV
- Modular architecture
  
## 🚀 Areas for Enhancement

- 🎯 Support for different fitness goals (bulk, cut, recomp)
- 📈 Historical analytics and trend visualization
- 🌍 Metric/imperial unit conversion
- ⚖️ Different calculation formulas or model selection
- 🧪 Comprehensive unit and integration tests
- 🐳 Docker containerization for easy deployment

## 🧩 Documentation

- **Project Overview** – See [overview.md](overview.md) for detailed project objectives and architecture.
- **Database Schema**– Inspect [database/models.py](database/models.py) for stored report structure.

## 👨‍💻 Author

**Atharva Shirodkar**

GitHub: https://github.com/atharvashirodkar

