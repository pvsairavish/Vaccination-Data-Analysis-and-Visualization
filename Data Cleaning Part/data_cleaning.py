import pandas as pd
import numpy as np

# ====================== LOAD DATA ======================
coverage = pd.read_excel("coverage-data.xlsx")
incidence = pd.read_excel("incidence-rate-data.xlsx")
reported_cases = pd.read_excel("reported-cases-data.xlsx")
vaccine_intro = pd.read_excel("vaccine-introduction-data.xlsx")
vaccine_schedule = pd.read_excel("vaccine-schedule-data.xlsx")

print("Data loaded successfully!\n")

# ====================== CLEANING ======================

# 1. Coverage
coverage = coverage.dropna(subset=['CODE', 'YEAR', 'ANTIGEN'], how='any')
coverage['YEAR'] = coverage['YEAR'].astype(int)
coverage_clean = coverage.dropna(subset=['COVERAGE'])

# 2. Incidence
incidence = incidence.dropna(subset=['CODE', 'YEAR', 'DISEASE'], how='any')
incidence['YEAR'] = incidence['YEAR'].astype(int)
incidence_clean = incidence.dropna(subset=['INCIDENCE_RATE'])

# 3. Reported Cases
reported_cases = reported_cases.dropna(subset=['CODE', 'YEAR', 'DISEASE'], how='any')
reported_cases['YEAR'] = reported_cases['YEAR'].astype(int)
reported_clean = reported_cases.dropna(subset=['CASES'])

# 4. Vaccine Introduction
vaccine_intro_clean = vaccine_intro.dropna(subset=['ISO_3_CODE', 'YEAR', 'DESCRIPTION'], how='any')
vaccine_intro_clean['YEAR'] = vaccine_intro_clean['YEAR'].astype(int)

# 5. Vaccine Schedule
vaccine_schedule_clean = vaccine_schedule.dropna(subset=['ISO_3_CODE', 'YEAR', 'VACCINECODE'], how='any')
vaccine_schedule_clean['YEAR'] = vaccine_schedule_clean['YEAR'].astype(int)

print("Cleaning completed!\n")

# ====================== SAVE CLEANED FILES ======================
print("Saving cleaned files...")

coverage_clean.to_excel("cleaned_coverage.xlsx", index=False)
incidence_clean.to_excel("cleaned_incidence.xlsx", index=False)
reported_clean.to_excel("cleaned_reported_cases.xlsx", index=False)
vaccine_intro_clean.to_excel("cleaned_vaccine_intro.xlsx", index=False)
vaccine_schedule_clean.to_excel("cleaned_vaccine_schedule.xlsx", index=False)

print("All cleaned files saved successfully!")
print("\nFiles created:")
print("1. cleaned_coverage.xlsx")
print("2. cleaned_incidence.xlsx")
print("3. cleaned_reported_cases.xlsx")
print("4. cleaned_vaccine_intro.xlsx")
print("5. cleaned_vaccine_schedule.xlsx")