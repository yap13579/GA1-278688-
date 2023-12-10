import pandas as pd
import os
import matplotlib.pyplot as plt 
import numpy as np

os.system("cls")
data = pd.read_excel(r"D:\pythonprogram\GA1Excel.xlsx",sheet_name="2022_3")
month=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
df=pd.DataFrame(data)
df['Month']=month
columnnames=list(df.columns.values)
print(df)
print(columnnames)
df=df.drop(columns=[ 'Jumlah / Total'])
print(df)



fig, axes = plt.subplots(nrows=4, ncols=3)
legend_labels = df.columns[1:]
for i, (_, row) in enumerate(df.iterrows()):
    sizes = row[1:].values.tolist()

    print(_)
    print(row)
    ax = axes[i // 3, i % 3]  
    ax.pie(sizes, labels=None, autopct='%1.1f%%', startangle=140)
    
    ax.set_title(f'Pie chart of each type of bank for {row["Month"]} in 2022', fontsize=12)  
    ax.axis('equal')  

fig.legend(labels= legend_labels, loc='upper right', fontsize=10, bbox_to_anchor=(1.1, 0.9)).set_draggable(True)  
plt.subplots_adjust(left=0.019, bottom=0.006, right=1, top=0.95, wspace=0.063, hspace=0.011)
plt.tight_layout()

plt.show()