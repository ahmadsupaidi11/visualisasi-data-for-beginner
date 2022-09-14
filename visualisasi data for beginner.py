from turtle import color, left
import pandas as pd
import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv('retail_raw_reduced.csv')
print('Ukuran dataset: baris %d dan %d kolom\n' % dataset.shape)
print('lima data teratas')
print(dataset.head())

dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').strftime('%Y-%m'))
print(dataset.head())

#penambahan kolom GMV, gmv adalah perkaliansetiap kolom item_price dan kolom quantity

dataset['gmv']= dataset['item_price']*dataset['quantity']
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas')
print(dataset.head())

#data agregat
monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()
print(monthly_amount)

#cara 1 membuat grafik
plt.plot(monthly_amount['order_month'], monthly_amount['gmv'])
plt.show()

#cara 2 dengan dataframe
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.show()

plt.figure(figsize=(10,5))
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.show()

plt.figure(figsize=(10,5))
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.title('Monthly GMV Year 2019', loc='center', pad=30, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total GMV', fontsize=15)
plt.show()

plt.figure(figsize=(10,5))
dataset.groupby(['order_month'])['gmv'].sum().plot(color='black', marker='o', linestyle='-.', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total GMV', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.show()

plt.figure(figsize=(10,5))
dataset.groupby(['order_month'])['gmv'].sum().plot(color='black', marker='o', linestyle='-.', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total GMV', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels,(labels/1000000000).astype(int))
plt.text(0.45, 0.72, 'The GMV increased significantly on October 2019', color='red')
plt.savefig('monthly_savefig.png')
plt.show()

plt.figure(figsize=(10,5))
dataset[dataset['order_month']=='2019-12'].groupby(['order_date'])['customer_id'].nunique().plot(color='blue',marker='.', linewidth=2)
plt.title('Daily Number of Customers - December 2019', loc='left', pad=20, fontsize=20, color='red')
plt.xlabel('Order Date', fontsize=15, color='blue')
plt.ylabel('Number of customer', fontsize=15, color='blue')
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
plt.show()