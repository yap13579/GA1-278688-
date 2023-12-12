import pandas as pd
import os
import matplotlib.pyplot as plt 
os.system("cls")
#replace directory with the current location of your excel file
data = pd.read_excel(r"D:\pythonprogram\GA1Excel.xlsx",sheet_name="2022_3")
month=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
df=pd.DataFrame(data)
columnnames=list(df.columns.values)

tl=df['Jumlah / Total']
df=df.drop(['Month'],axis=1)
df.insert(0,'Month',month)

df=df.drop(['Jumlah / Total'],axis=1)

ax=df.plot(kind="bar",ylabel='RM million',xlabel='Month',stacked=True,width=0.8,figsize=(30,8))
ax.bar_label(ax.containers[len(ax.containers)-1],labels=[f'RM{x:.2f}'for x in tl],fontsize=8)
ax=tl.plot(kind='line', marker='x', color='red', ms=10,linestyle='--')
plt.xticks(df.index,month,fontsize=10)
plt.legend(loc="upper center",fontsize=10).set_draggable(True)
plt.title('Loan/Financing Applied each Banking Type by month in 2022')

plt.show()