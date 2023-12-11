import pandas as pd
import os
import matplotlib.pyplot as plt 
os.system("cls")
#replace directory with the current location of your excel file
data = pd.read_excel(r"D:\pythonprogram\GA1Excel.xlsx",sheet_name="2023_1")
month=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
df=pd.DataFrame(data)
columnnames=list(df.columns.values)

tl=df['Total Loan/Financing Applied']
df=df.drop(['Overall Total','Total Loan/Financing Applied'],axis=1)
df.insert(0,'Month',list(month[0:9]))



ax=df.plot(kind="barh",ylabel='Month',xlabel='RM million',stacked=True,width=0.8,figsize=(30,8))
ax.bar_label(ax.containers[len(ax.containers)-1],labels=[f'RM{x:.2f}'for x in tl],fontsize=8)

plt.yticks(df.index,list(month[0:9]),fontsize=10)
plt.legend(loc="upper center",fontsize=10).set_draggable(True)
plt.title('Loan/Financing Applied each Banking Type by month in 2023')

plt.show()