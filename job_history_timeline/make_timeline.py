import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime



experiences = [
    ["Job Title2,\nCompany2", "2023-06-01", "2024-07-01"],
    ["Job Title1,\nCompany1", "2020-09-01", "2023-05-01"],
    ["Volunteering,\nOrganization", "2018-07-01", "2020-03-01"],
    ["Degree,\nUniversity", "2016-08-01", "2020-07-01"],
]



converted_experiences = []
for label,start_date,end_date in experiences:
    start_num = mdates.date2num(datetime.strptime(start_date, "%Y-%m-%d"))
    end_num = mdates.date2num(datetime.strptime(end_date, "%Y-%m-%d"))
    converted_experiences.append([label, start_num, end_num])



converted_experiences.sort(key=lambda x: x[1], reverse=True)



fig,ax = plt.subplots(figsize=(15,7))

# newest to oldest by startdate
colors = ['lightblue', 'lightblue', 'palegreen', 'lightgrey']



for i, (label,start,end) in enumerate(converted_experiences):
    color = colors[i]
    ax.barh(i, end - start, left=start, color=color, edgecolor='gray')
    ax.text((start + end) / 2, i, label, ha='center', va='center', fontsize=10, fontweight='bold', fontname='Arial', color='black')

# setting and formatting dates
ax.set_xlim([mdates.date2num(datetime(2016, 1, 1)), mdates.date2num(datetime(2024, 6, 1))])
ax.xaxis_date()
date_format = mdates.DateFormatter('%Y')
ax.xaxis.set_major_formatter(date_format)


# cleaning things up
ax.grid(True, axis='x', linestyle='--', alpha=0.7)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_yticks(range(len(converted_experiences)))
ax.set_yticklabels([]) 

# plt.show()

plt.tight_layout()
plt.savefig('job_history.png', dpi=500)



