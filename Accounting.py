#讀取檔案
products = []
with open('products.csv', 'r', encoding= 'utf-8') as f:
	for line in f:
		if '商品名稱,價格' in line :
			continue
		name, price = line.strip().split(',') #以,為切割標準
		products.append([name, price])
print(products)
#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
	price = int (price) #假設把價格改成整數
print (products)
#列出購買紀錄
for p in products:
	print(p[0],'的價格是',p[1])
#寫入檔案
with open('products.csv', 'w',encoding= 'utf-8') as f:  #encoding 改編碼成 utf-8
	f.write('商品名稱,價格\n')
	for p in products:
		f.write(p[0]+',' + str(p[1]) +'\n')  #str改成字串 