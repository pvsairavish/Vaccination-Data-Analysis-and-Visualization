# Vaccination-Data-Analysis-and-Visualization

# 💉 Vaccination Data Analysis & Visualization

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![SQL](https://img.shields.io/badge/SQL-SQLite-orange)
![Power%20BI](https://img.shields.io/badge/Power%20BI-Interactive%20Dashboards-yellow)
![Status](https://img.shields.io/badge/Status-Completed-success)

### Data Cleaning • SQL Database • Exploratory Data Analysis • Power BI Dashboards

---

## 📌 Project Overview

**Vaccination Data Analysis and Visualization** is an end-to-end data analytics project focused on understanding global vaccination coverage, disease incidence, and the effectiveness of immunization programs.

The project involves:

1. **Data Cleaning** using Python (Pandas)
2. **Structured Storage** using SQLite Database
3. **Exploratory Data Analysis (EDA)** with 15+ meaningful charts
4. **Interactive Dashboards** created in Power BI

The goal is to generate actionable insights that can support public health decision-making, resource allocation, and policy formulation.

---

## 🎯 Business Objectives

- Assess the effectiveness of vaccination programs across countries and regions
- Identify regions with low vaccination coverage for targeted interventions
- Analyze the relationship between vaccine introduction and disease reduction
- Support data-driven public health strategies and resource allocation
- Track progress toward global immunization goals

---

## 🗂️ Dataset

The project uses five related datasets:

| File                          | Description                                              |
|------------------------------|----------------------------------------------------------|
| coverage-data.xlsx           | Vaccination coverage, doses, target population by country and antigen |
| incidence-rate-data.xlsx     | Disease incidence rates                                  |
| reported-cases-data.xlsx     | Number of reported disease cases                         |
| vaccine-introduction-data.xlsx | Vaccine introduction status (Yes/No) by country        |
| vaccine-schedule-data.xlsx   | Recommended vaccination schedules                        |

**Source:** WHO-style public health vaccination data

---

## 🛠️ Tech Stack

- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **SQLite** (Database)
- **Power BI** (Interactive Dashboards)
- **Google Colab / VS Code** (EDA & Cleaning)
- **DB Browser for SQLite**

---

## 📁 Project Structure
Vaccination_Project/
│
├── data/
│ ├── original/ # Original Excel files
│ └── cleaned/ # Cleaned Excel files
│
├── database/
│ └── Vaccination_Project.db # SQLite Database
│
├── notebooks/
│ └── Vaccination_EDA.ipynb # Exploratory Data Analysis
│
├── powerbi/
│ └── Vaccination_Dashboard.pbix
│
├── scripts/
│ ├── data_cleaning.py
│ └── load_to_sqlite.py
│
└── README.md
text---

## 🧠 Project Pipeline

### 1. Data Cleaning (Python)
- Handled missing values
- Converted Year to integer
- Removed incomplete records
- Created clean versions of all five datasets

### 2. SQL Database Design
- Created normalized tables:
  - coverage
  - incidence
  - reported_cases
  - vaccine_introduction
  - vaccine_schedule
- Loaded cleaned data into SQLite

### 3. Exploratory Data Analysis (EDA)
Performed detailed EDA with 15+ charts including:
- Coverage trends over years
- Top countries by coverage
- Disease incidence trends
- Top diseases by incidence
- Vaccine introduction status
- Correlation between coverage and incidence
- WHO Region analysis
- Heatmaps and pair plots

### 4. Power BI Dashboards
Created 3 interactive pages:

**Page 1 – Coverage Overview**
- KPI Cards
- Coverage trend over years
- Top 10 countries
- Coverage by Antigen

**Page 2 – Disease Analysis**
- Incidence trends
- Top diseases by incidence
- Reported cases over time
- Incidence vs Cases relationship

**Page 3 – Vaccine Introduction**
- Introduction status (Yes vs No)
- Top vaccines by countries introduced
- WHO Region comparison

---

## 📊 Key Insights

- Vaccination coverage has shown an overall increasing trend over the years
- Higher vaccination coverage is associated with lower disease incidence
- Significant disparities exist across countries and WHO regions
- Some diseases still show high incidence despite vaccine availability
- Early vaccine introduction is linked to faster reduction in disease cases

---

## 💡 Recommendations

1. Prioritize low-coverage countries and regions for targeted interventions
2. Strengthen monitoring of high-incidence diseases
3. Accelerate vaccine introduction in lagging WHO regions
4. Improve follow-up to reduce drop-off between doses
5. Use interactive dashboards for continuous progress tracking

---

## ⚙️ How to Run the Project

### 1. Data Cleaning
```bash
python data_cleaning.py
2. Load Data into SQLite
Bashpython load_to_sqlite.py
3. Exploratory Data Analysis

Open Vaccination_EDA.ipynb in Google Colab or Jupyter
Run all cells

4. Power BI Dashboard

Open Vaccination_Dashboard.pbix
Refresh data if required


📈 Tools & Skills Demonstrated

Data Cleaning & Preprocessing
SQL Database Design & Querying
Exploratory Data Analysis
Data Visualization
Interactive Dashboard Development
Public Health Analytics


✨ Future Improvements

Add geographical maps in Power BI
Include more granular (monthly) data if available
Build predictive models for coverage forecasting
Deploy dashboard on Power BI Service
Create a Streamlit version of key insights


👨‍💻 Author
Punati Venkata Sai Ravish
