import pandas as pd
import os
import matplotlib.pyplot as plt 
import numpy as np

os.system("cls")
data = pd.read_excel(r"D:\pythonprogram\GA1Excel.xlsx",sheet_name="2023_1")
month=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
df=pd.DataFrame(data)
columnnames=list(df.columns.values)

xm=month[0:9]
x=[0,1,2,3,4,5,6,7,8]

y=np.array(df['Total Loan/Financing Applied'])

plt.plot(xm,y,color='b',marker='x',linestyle='-', linewidth=2, markersize=8)
plt.xlabel("Month")
plt.ylabel('RM million')
z=np.polyfit(x,y,1)
p=np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.legend(["Total Loan/Financing Applied","Trend Line"],loc="best").set_draggable(True)
for xs, ys in zip(x, y):
    plt.text(xs, ys, str(f'RM{ys:.2f}'), color="black", fontsize=12)

plt.grid(True)
plt.title('Total Loan/Financing Applied by Banking Type each month in 2023')
plt.show() 
