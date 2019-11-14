import os 
#讀取檔案
def read_file(filesname):
	products = []
	with open(filesname, 'r', encoding='utf-8') as f:
			for line in f:
				if '商品名稱,價格' in line :
					continue
				name, price = line.strip().split(',') #以,為切割標準
				products.append([name, price])
	return products
#讓使用者輸入
def input_file(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		products.append([name, price])
		price = int (price) #假設把價格改成整數
	print (products)
	return(products)
#列出購買紀錄
def buy_file(products):
	for p in products:
		print(p[0],'的價格是',p[1])
#寫入檔案
def write_file(filesname,products):
	with open(filesname, 'w',encoding='utf-8') as f:  #encoding= 'utf-8'encoding 改編碼成 utf-8
		f.write('商品名稱,價格\n')
		for p in products:
			f.write(p[0]+',' + str(p[1]) +'\n')  #str改成字串 

def main():
	products = []
	filesname = 'products.csv'
	if os.path.isfile(filesname):
		print('Yeah!')
		products = read_file(filesname)
	else:
		print('Woops!')
	products = input_file(products)
	buy_file(products)
	write_file('products.csv', products)
	

main() 
