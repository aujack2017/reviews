data = []
count = 0
wc = {}

def read_file(filename):
	data = []
	count = 0
	with open(filename,'r',encoding='utf-8-sig') as f:
		for line in f:
			data.append(line)
			count += 1
			if count % 1000 == 0:
				print('現在讀取了', count , '筆了')
		print('檔案讀取完了, 共讀取', len(data), '筆資料')
		return data

def word_count(data):
	wc = {}  #word_count
	for d in data:
		words = d.split()
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1
	return wc
	#print(words)
	#break
for d in wc:
	if wc[d] > 1000000:
		print(d, '出現的次數共：', wc[d])

def find_word(wc):
	while  True:
		d = input('請輸入要查詢的字串：')
		if d == 'q':
			print('感謝使用此功能!!!')
			break

		if d in wc:
			print(d, '出現的次數為：', wc[d])
		else:
			print('你要查詢的字串：', d, ' 不在字典檔裡。')

def main():
	data = read_file('reviews.txt')
	wc = word_count(data)
	#d = input('請輸入要查詢的字串：')
	find_word(wc)

main()

#print(wc)


# sum_len = 0
# new = []
# for d in data:
# 	if (len(d)) < 100:
# 		new.append(d)
# print('留言長度小於100的有', len(new), '筆')
# print('留言長度大於100的有', len(data)-len(new), '筆')

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('留言中包含 good字串的留言有', len(good), '筆')


