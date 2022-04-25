from googletrans import Translator
translator = Translator()
out = translator.translate('Hallo?',src="de",dest="ja")

print(out)
print(u'\u30af\u30a4\u30c3\u30af\u30b9\u30bf\u30fc\u30c8\u30ac\u30a4\u30c9\u30A0')
