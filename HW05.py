
#1
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October' 'November', 'December']
for m in months:
    if m.startswith('J'): #m.startswith return the letter that the string starts
        print(m)
#2
for i in range(0,100):
    if i % 2 == 0 and i % 5 == 0 :
        print(i)
#3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
for h in horton:
    for v in vowels:
        if v == h :
            print(v)

