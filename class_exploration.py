import pandas as pd
import numpy as np

df = pd.DataFrame.from_csv('NA_ALL_20170831_08a.csv', encoding = "ISO-8859-1")

df2 = pd.DataFrame.from_csv('reports/Courses_with_Affected_Profs_2017-08-31-08a.csv')

df2[['SUBJ', "TTL ENRL"]].head()

import matplotlib.pyplot as plt

total_enrollment_by_subj = df2.groupby(['SUBJ'])['TTL ENRL'].sum()
total_enrollment_by_subj
total_enrollment_by_subj = total_enrollment_by_subj.sort_values(ascending=False)
subjects = list(total_enrollment_by_subj.index)
subjects_pos = np.arange(len(subjects))
# plt.bar(subjects_pos, total_enrollment_by_subj.values, align='center', alpha=.5)
# plt.hist(subjects_pos, len(subjects), weights=total_enrollment_by_subj.values)
# plt.xticks(subjects_pos, subjects, rotation='vertical')
# # plt.autoscale()
# plt.savefig('total_enrollment_by_subject.png')
# plt.show()
import seaborn as sns
data = total_enrollment_by_subj.to_frame().reset_index()
data.columns = ['Subject', 'Total Enrollment']
plt.figure(figsize=(20,15))
sns.set(font_scale=1.3)
sns.barplot(x='Subject', y='Total Enrollment', data=data)
plt.xticks(rotation=90)
plt.show()
