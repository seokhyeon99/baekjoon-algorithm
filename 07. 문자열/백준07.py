#11654
import sys
a = sys.stdin.readline().strip()
print(ord(a))

#11720
import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
sum = 0
for i in range(int(a)):
    sum += int(b[i:i+1])
print(sum)

#10809
import sys
a = sys.stdin.readline().strip()
for i in range(97,123):
    print(a.find(chr(i)), end=" ")

#2675
import sys
a = sys.stdin.readline().strip()
for i in range(int(a)):
    b,c = sys.stdin.readline().strip().split()
    for j in range(len(c)):
        for k in range(int(b)):
            print(c[j:j+1], end='')
    print()


#1157
import sys
a = sys.stdin.readline().strip()
count = [0]*26
for i in range(len(a)):
    if ord(a[i:i+1])>=65 and ord(a[i:i+1])<=90:
        count[ord(a[i:i+1])-65] += 1
    elif ord(a[i:i+1])>= 97 and ord(a[i:i+1]) <=122:
        count[ord(a[i:i+1]) - 97] += 1
first = max(count)
first_index = count.index(first)
count.pop(first_index)
second = max(count)
if first == second:
    print('?')
else:
    print(chr(first_index+65))
    
#1152
import sys
a = sys.stdin.readline().strip()
count = 0
for i in range(len(a)):
    if a[i:i+1] == ' ':
        count += 1
if a == ' '*len(a):
  print('0')
else:
  print(count+1)
  
#2908
import sys
a,b = sys.stdin.readline().strip().split()
c=0
d=0
for i in range(3):
    c += int(a[i:i+1]) * (10**(i))
    d += int(b[i:i+1]) * (10**(i))
if c>d:
    print(c)
else:
    print(d)
    
#5622
import sys
a = sys.stdin.readline().strip()
time = 0
for i in range(len(a)):
    if 65<=ord(a[i:i+1])<=67:
         time += 3
    elif (68<=ord(a[i:i+1])<=70):
         time += 4
    elif (71<=ord(a[i:i+1])<=73):
         time += 5
    elif (74<=ord(a[i:i+1])<=76):
         time += 6
    elif (77<=ord(a[i:i+1])<=79):
         time += 7
    elif (80<=ord(a[i:i+1])<=83):
         time += 8
    elif (84<=ord(a[i:i+1])<=86):
         time += 9
    elif (87<=ord(a[i:i+1])<=90):
         time += 10
print(time)
