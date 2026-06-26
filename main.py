import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
np.random.seed(42)
days=np.arange(1,31)#30 days of work 
sales=np.random.randint(50,150,size=30)#30 sales in the 30 days of the work
costs=np.random.randint(10,45,size=30)

data={
    "days":days,
    "sales":sales,
    "costs":costs,
    "profit":sales-costs,
    
}

table=pd.DataFrame(data)
print(table)
print("_"*70)
total_profit=table["profit"].sum()
print("total profit is ------->",total_profit)


plt.figure(figsize=(20,10))
plt.plot(table["days"],table["sales"],label="sales",marker="o",linestyle="-",color="blue")
plt.plot(table["days"],table["costs"],label="costs",marker="s",linestyle="--",color="red")
plt.plot(table["days"],table["profit"],label="profit",marker="^",linestyle="--",color="green")
plt.title("company analysis")
plt.xlabel("days")
plt.ylabel("count")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
