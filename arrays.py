# array bkol basata hiya wa7d sndo9 kitkown mn 4 d lblas t9dr t7ot fihom valeur
# ila wsl l7ad deal o 3mr o bghiti t3awd tzid fih kidobl lblas li 3ado ya3ni gha
# iwlii 8 mn ba3d 16 o ghadi b7alk haka 

arr = []

for i in range(6):
        arr.append(i)
    
# dima index kibda mn 0 machi 1
print(arr)

# ila bghiti ghi value wa7da kat5od l indice dealha
print(arr[2])  # O(1)

# ila bghiti tm7i chi value
del arr[3]  # O(n)
# o n9dro ndiro 7ta arr.pop(3)

# ila bghiti t9lb 3la chi 9ima  o t5od l indice dealha
arr.index(3)   # O(n)
# ila kant value makaynach f arr katrod lk -1

''' kaynin bzzf d tor9 bach ndiro array o imkn arr tkon fiha arr katsma
    2D array , tor9 homa :
      arr = [1,3,4] 
      arr = [1,2] + [3,4]
      arr = [0]*10
      arr = list(range(100))
      arr = [['ndjek'],['enke'],['enee']]'''
'''
# n9droo ndiro des operations f arr
len(arr)
arr.append(value)
arr.remove(3)
arr.insert(3,4)   
min(arr),max(arr)
arr.reverse()
reversed(arr)
arr.sort()
sorted(arr)    '''

# n9dro n5dmo b in 
#n9dro nchofo wach kayna chi value f aaray o la la 
5 in arr  # hadi gha trod lina true or false O(n)

# silicing o hiya wa7ad l5asiya f arr li n9dro fiha na5odo ghi wa7d partie mn arr
# arr[start:end:step]



