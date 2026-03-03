import pandas as pd
df = pd.read_csv("C:/Users/Al Kareem Traders/Desktop/Data Science/Final Projects/Hr analystics - employee attrition/Data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
# print(df)
# print(df.info())
#                               Overall Situation
df_attrition = df[df["Attrition"]=="Yes"]
total_rows = df["Attrition"].count()
# print(total_rows) # 1470
total_Attrition = df[df["Attrition"]=="Yes"].shape[0]
# print(total_Attrition) # 237
attrition_rate = (total_Attrition/total_rows)*100
# print(attrition_rate.round(2)) # 16.12
overall_summary = pd.DataFrame({
    "Total_Employees": [total_rows],
    "Total_Attrition": [total_Attrition],
    "Attrition_Rate_%": [attrition_rate]
})
# print(overall_summary)
# overall_summary.to_csv("overall_summary.csv",index=False)


marital_status = df_attrition.groupby("MaritalStatus").size().reset_index(name="Attrition_count").sort_values(by="Attrition_count",ascending=False)
# print(marital_status)
# marital_status.to_csv("Marital_status vs Arrition.csv",index=False)

# Gender wise
gender_wise_attrition = df_attrition.groupby("Gender").size().reset_index(name="Attrition_count").sort_values(by="Attrition_count",ascending=False)
# print(gender_wise_attrition)
# gender_wise_attrition.to_csv("Gender vs Attrition.csv",index=False)

# Age wise
age_wise = df_attrition.groupby("Age").size().reset_index(name="Attrition_count").sort_values(by="Age",ascending=True)
# print(age_wise)

bins = [18,28,39,50,58]
labels = ["18-28","29-39","40-50","51-58"]
df["Age_group"] = pd.cut(df["Age"],bins=bins,labels=labels,right=True,include_lowest=True)
# print(df["Age_group"])
age_attrition = df[df["Attrition"]=="Yes"]
ageGroup_vs_attrition = age_attrition.groupby("Age_group").size().reset_index(name="Attrition_count")
# print(ageGroup_vs_attrition)
# ageGroup_vs_attrition.to_csv("Age group vs Attrition.csv",index=False)

# Department Wise
dept_summary = (
    df.groupby("Department").agg(
          Total_Employees=("EmployeeNumber", "count"),
          Attrition_Count=("Attrition", lambda x: (x == "Yes").sum()),
          Stayed_Count=("Attrition", lambda x: (x == "No").sum())).reset_index())
# print(dept_summary)
# dept_summary.to_csv("Dept_summary.csv",index=False)


# Education background wise attrition
edu_background_wise = df_attrition.groupby("EducationField").size().reset_index(name="Attrition_count").sort_values(by="Attrition_count",ascending=False)
# print(edu_background_wise)
# edu_background_wise.to_csv("Edu_background_wise.csv",index=False)

# Environment Satisfaction impact
Env_Satisfaction_wise = df_attrition.groupby("EnvironmentSatisfaction").size().reset_index(name="Attrition_count").sort_values(by="Attrition_count",ascending=False)
# print(Env_Satisfaction_wise)
# Env_Satisfaction_wise.to_csv("Env_satisfaction_wise.csv",index=False)

# job level & job role & jobsatisfaction
job_role_wise = df_attrition.groupby("JobRole").size().reset_index(name="Attrition_count").sort_values(by="Attrition_count",ascending=False)
# print(job_role_wise)
# job_role_wise.to_csv("Job_role_wise.csv",index=False)

job_level_wise = df_attrition.groupby("JobLevel").size().reset_index(name="Attrition_count").sort_values(by="Attrition_count",ascending=False)
# print(job_level_wise) # imp for visual
# job_level_wise.to_csv("Job_level_wise.csv",index=False)

job_statisfaction_wise = df_attrition.groupby("JobSatisfaction").size().reset_index(name="Attrition_count").sort_values(by="Attrition_count",ascending=False)
# print(job_statisfaction_wise)

data = df
job_satisfaction_detail = pd.pivot_table(
    data,
    index="JobRole",
    columns="JobSatisfaction",
    values="EmployeeNumber",
    aggfunc="count",
    fill_value=0
)
job_satisfaction_detail["Total"] = job_satisfaction_detail.sum(axis=1)
job_satisfaction_detail = job_satisfaction_detail.reset_index()
print(job_satisfaction_detail)
# job_satisfaction_detail.to_csv("Job_satisfaction_detail2.csv",index=False)

# jobinvolvement
jobInvolvement_vs_attrition = df_attrition.groupby("JobInvolvement").size().reset_index(name="Attrition_count").sort_values(by="Attrition_count",ascending=False)
# print(jobInvolvement_vs_attrition)# no impact on attrition

#   Relationship satisfaction impact on attrition
relationshipSatisfaction_vs_attrition = df_attrition.groupby("RelationshipSatisfaction").size().reset_index(name="Attrition_count").sort_values(by="Attrition_count",ascending=False)
# print(relationshipSatisfaction_vs_attrition) # no impact

# Overtime impact on attrition
overtime_impact = df_attrition.groupby("OverTime").size().reset_index(name="Attrition_count").sort_values(by="Attrition_count",ascending=False)
# print(overtime_impact)# no impact on 

# monthly income vs Attrition
monthlyRate_avg = df["MonthlyRate"].mean().round(2)
# print(monthlyRate_avg)
# df["MonthlyIncomeAvg"] = df["MonthlyRate"].apply(
#     lambda x:"Below Avg" if x <monthlyRate_avg else "Above Avg"
# )
# print(df["MonthlyIncomeAvg"])
# monthlyIncome_vs_attrition = df[df["Attrition"]=="Yes"]["MonthlyIncomeAvg"].value_counts()
# print(monthlyIncome_vs_attrition) # no Salary impact on attrition
percentSalaryHike_avg = df["PercentSalaryHike"].mean().round(2)
# print(percentSalaryHike_avg)
df["HikeGroup"] = df["PercentSalaryHike"].apply(
    lambda x:"Low Hike" if x<percentSalaryHike_avg else "High Hike"
)
percentSalaryHike_vs_attrition = pd.crosstab(df["HikeGroup"], df["Attrition"])
# print(percentSalaryHike_vs_attrition) # imp
percentSalaryHike_vs_attrition = percentSalaryHike_vs_attrition.reset_index()
# percentSalaryHike_vs_attrition.to_csv("Percent_salary_hike_vs_attrition.csv",index=False)


# years since last promotion vs attrition
year_since_l_promo_vs_attrition = df_attrition.groupby("YearsSinceLastPromotion").size().reset_index(name="Attrition_count").sort_values(by="Attrition_count",ascending=False).head(7)
print(year_since_l_promo_vs_attrition) # imp
year_since_l_promo_vs_attrition.to_csv("year since last promotionn vs attrition.csv",index=False)

# total working years vs attrition
totalWorkingYears_vs_attrition = df_attrition.groupby("TotalWorkingYears").size().reset_index(name="Attrition_count").sort_values(by="Attrition_count",ascending=False).head(5)
# print(totalWorkingYears_vs_attrition) # imp
# totalWorkingYears_vs_attrition.to_csv("Total working years vs attrition.csv",index=False)