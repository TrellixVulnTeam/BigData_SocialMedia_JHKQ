import matplotlib.pyplot as plt 
from collections import Counter


plt.subplot(111, facecolor='w')
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}

# Show family options

families = []
myf =  open ("C:/Users/tammy/Documents/python/wow.txt")
line = myf.read()
words = line.split()
for w in words:
     families.append(w)

wordcount = Counter(families)
print(wordcount.most_common(6))
t = plt.text(0.0, 0.9, 'Hot Topics World Cup', size='large', **alignment)

yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

for k, family in enumerate(wordcount.most_common(6)):
    t = plt.text(0.0, yp[k], family, family=family, **alignment)


x = -0.4
# Show bold italic


plt.axis([-1, 1, 0, 1])
plt.show()