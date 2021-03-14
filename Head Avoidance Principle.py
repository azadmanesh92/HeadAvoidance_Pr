


# Head-Avoidance Principle

# Author: Mahsa Azadmanesh
# Sharif University
# StdNum: 94202577


print('به نام خدا')
print('')
print('_تشخيص تکيه ي عبارت با استفاده از اصل هسته گريزي_')
print('')
#ليست صفت ها:
#adj1={'خوب','کوشا','زيبا','توانا','مهربان','سرسبز','زيباي','کوشاي','تواناي'}
#adj2={'سفيد','سياه','قرمز','آبي','سبز','نارنجي','زرد','بنفش','خاکستري','نبلي','صورتي'}
#adj3={'طولاني','کوتاه','روشن','تاريک','بزرگ','کوچک','نازک','ضخيم','مرتفع','عميق','سرد','گرم','باز','بسته'}
#adj4={'بهتر','کوشاتر','زيباتر','مهربانتر','سرسبزتر'}
#adj4={'بهترين','کوشاترين','زيباترين','مهربانترين','سرسبزترين','تواناتر'}
#adj5={'هيچ','هر','همان','بعضي','برخي','همه','همه ي','تمام','بي شمار','بيشمار'}

#intNum={'يک','دو','سه','جهار','پنج','شش','هفت','هشت','نه','ده','صد','هزار','ميليون','ده ها','صدها','هزاران','ميليونها','بي نهايت','بينهايت'}
#floatNum={'نيم','يک و نيم','دو و نيم','سه و نيم','چهار و نيم','پنج و نيم','شش و نيم','هفت و نيم','هشت و نيم','نه و نيم','ده و نيم'}
#ordNum={'اولين','اول','آخرين','آخر','دومين','دوم','سومين','سوم','چهارمين','چهارم','پنجمين','پنجم','ششمين','ششم','هفتمين','هفتم','هشتمين','هشتم','نهمين','نهم','دهمين','دهم','صدمين','صدم','هزارمين','هزارم'}



word_list = ['خوب','کوشا','زيبا','توانا','مهربان','سرسبز','زيباي','کوشاي','تواناي','سفيد','سياه','قرمز','آبي','سبز','نارنجي','زرد','بنفش','خاکستري','نبلي','صورتي','طولاني','کوتاه','روشن','تاريک','بزرگ','کوچک','نازک','ضخيم','مرتفع','عميق','سرد','گرم','باز','بسته','بهتر','کوشاتر','زيباتر','مهربانتر','سرسبزتر','بهترين','کوشاترين','زيباترين','مهربانترين','سرسبزترين','تواناتر','هيچ','هر','همان','بعضي','برخي','همه','همه ي','تمام','بي شمار','بيشمار','يک','دو','سه','جهار','پنج','شش','هفت','هشت','نه','ده','صد','هزار','ميليون','ده ها','صدها','هزاران','ميليونها','بي نهايت','بينهايت','نيم','يک و نيم','دو و نيم','سه و نيم','چهار و نيم','پنج و نيم','شش و نيم','هفت و نيم','هشت و نيم','نه و نيم','ده و نيم','اولين','اول','آخرين','آخر','دومين','دوم','سومين','سوم','چهارمين','چهارم','پنجمين','پنجم','ششمين','ششم','هفتمين','هفتم','هشتمين','هشتم','نهمين','نهم','دهمين','دهم','صدمين','صدم','هزارمين','هزارم']


input_string = input('عبارت خود را وارد کنيد: ')
input_string = input_string.split()



#تشخيص هسته و وابسته:

index = input_string.index(list(set(input_string) - set(word_list))[0])

print ('ايندکس هسته ',index,'است')
w_range = []
for item in range(len(input_string)):
	w_range.append(abs(index - item))
output = input_string[w_range.index(max(w_range))]
print ('تکيه ي عبارت روي: ',output)



