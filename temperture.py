x = input('請問攝氏轉華氏，還是華氏轉攝氏｜攝氏輸入c、華氏輸入f:') #確認所需功能

if x == 'c':
    c = input('攝氏溫度轉換，請輸入攝氏溫度:')#要求輸入溫度
    c = float(c) #casting，使用者可能會輸入小數
    f = c * 9 / 5 + 32 #溫度轉換
    print('華氏溫度為',f)
elif x == 'f':
    f = input('攝氏溫度轉換，請輸入華氏溫度:')#要求輸入溫度
    f = float(f) #casting，使用者可能會輸入小數
    c = (f - 32) / 9 * 5#溫度轉換
    print('攝氏溫度為',c)
else:
	print('你在供三小')