products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
	price = int (price) #假設把價格改成整數
print (products)

for p in products:
	print(p[0],'的價格是',p[1])

with open('products.csv', 'w',encoding= 'utf-8') as f:  #encoding 改編碼成 utf-8
	for p in products:
		f.write(p[0]+',' + str(p[1]) +'\n')  #str改成字串 