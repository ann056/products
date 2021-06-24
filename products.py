import os # operating system作業系統

# 讀取檔案
def read_file(filename):	
	products = []	
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
		print(products)
	return products

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品：')
		if name == 'q':
			break
		price = input('請輸入價格：')
		products.append([name, price])
		# 省略
		# p = []
		# p.append(name, price)
	print(products)
	return products


# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])
		# products清單中的小清單p，p中的第0個項目
	# 只是印東西，沒有要回傳，所以不用加return


# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')
			# w進f清單中，一定要用+ ',' 來分隔，\n是換行

def main():
	products = []	
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('找到檔案！')
		products = read_file(filename)
	else:
		print('檔案找不到！')
	products = user_input(products)
	print_products(products) # 沒有要回傳，所以不需儲存
	write_file(filename, products) # 沒有要回傳，所以不需儲存

main()
