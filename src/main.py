import pandas as pd
import os

excel_files = os.listdir("data")
print(excel_files)

relevant_cols = [
    "CASE_STATUS",
    "RECEIVED_DATE",
    "DECISION_DATE",
    "JOB_TITLE",
    "SOC_CODE",
    "SOC_TITLE",
    "BEGIN_DATE",
    "END_DATE",
    "EMPLOYER_NAME",
    "EMPLOYER_CITY",
    "EMPLOYER_STATE",
    "WAGE_RATE_OF_PAY_FROM",
]

excel = pd.read_excel(
    pd.read_excel(os.path.join("data", "LCA_Disclosure_Data_FY2022_Q2.xlsx"))
)[relevant_cols]
print(excel)
# excel_pandas = [pd.read_excel(os.path.join("data", f)) for f in excel_files]
