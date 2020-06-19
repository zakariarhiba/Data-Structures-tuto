# hiya wa7d l7ala 5asa mn list
# ya3ni b7al wa7d list mn char li n9dro ndiro ga3 app d list
# o 7ta houya b7al tuple mat9dr tbdl char dealo

# sntyax str
string = 'zakaria'

# ila bghiti tzid 3lih chi value python kaysayb var jdid o ki7ot fih str bvalue jdida

print(string[2])

s = '     abcd    '

# ila bghina n7aydo l espace 
s = s.strip()
print(s)

# n9dro nchofo wach kibda bchi value
s.startswith('ab')  # gha trod true or false
# 7ta wach katsali b chi value
s.endswith('de')

# n9droo n9smo wa7d l string o irj3 list o n5taro bach i9sm
noun = "zakaria,rhiba,hello".split(',')
print(noun)

# n9dro 7ta njm3o list f string 
print(','.join(['hello','world']))


# kaynin bzzf d les method n9dro ndirhom b string 
# ila bghit t3rfhom kamlin dir ghir  'print(dir(string))'
# gha itl3o lk ga3 function li t9dr dir wlkn kayna method bach t3rf kola 7aja o lach katli9
# dir 'help(function li bghiti t3rf 3liha hna)
