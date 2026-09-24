import pandas as pd
import sqlite3

# Connect to the database
conn = sqlite3.connect("Vaccination_Project.db")

print("Connected to database successfully!")

# Correct paths (because files are inside a folder)
coverage = pd.read_excel("C:\\Users\\punat\\OneDrive - Vignan University\\Desktop\\Vaccination_Project\\After Data Cleaning Excel files\\cleaned_coverage.xlsx")
incidence = pd.read_excel("C:\\Users\\punat\\OneDrive - Vignan University\\Desktop\\Vaccination_Project\\After Data Cleaning Excel files\\cleaned_incidence.xlsx")
reported_cases = pd.read_excel("C:\\Users\\punat\\OneDrive - Vignan University\\Desktop\\Vaccination_Project\\After Data Cleaning Excel files\\cleaned_reported_cases.xlsx")
vaccine_intro = pd.read_excel("C:\\Users\\punat\\OneDrive - Vignan University\\Desktop\\Vaccination_Project\\After Data Cleaning Excel files\\cleaned_vaccine_intro.xlsx")
vaccine_schedule = pd.read_excel("C:\\Users\\punat\\OneDrive - Vignan University\\Desktop\\Vaccination_Project\\After Data Cleaning Excel files\\cleaned_vaccine_schedule.xlsx")

print("Cleaned files loaded!")

# Import into SQLite tables
coverage.to_sql("coverage", conn, if_exists="append", index=False)
print("Coverage data imported!")

incidence.to_sql("incidence", conn, if_exists="append", index=False)
print("Incidence data imported!")

reported_cases.to_sql("reported_cases", conn, if_exists="append", index=False)
print("Reported Cases data imported!")

vaccine_intro.to_sql("vaccine_introduction", conn, if_exists="append", index=False)
print("Vaccine Introduction data imported!")

vaccine_schedule.to_sql("vaccine_schedule", conn, if_exists="append", index=False)
print("Vaccine Schedule data imported!")

conn.close()
print("\nAll data imported successfully into SQLite!")