
#1
def safeOpen(filename):
    try:
        file = open(filename,'r')
    except:
        file = None
    return file
inputFile = safeOpen('ghost.txt')
print(inputFile)

#2
def safeFloat(x):
    try:
        a = float(x)
        return a
    except ValueError:
        return 0.0
f = safeFloat('abc')
print(f)

#3
def averageSpeed():
    filename = input("Enter file name: ")
    file = safeOpen(filename)
    if file == None:
        print("File not found. Please try again")
        filename = input("Enter file name: ")
        file = safeOpen(filename)
        if file == None:
            print("File not found. Yet another human error. Goodbye.")
            return None
    content = file.readlines()
    speed = []
    for i in content:
        clean_i = i.split()
        for j in clean_i:
            if safeFloat(j) > 2.0:
                speed.append(safeFloat(j))
    avg_speed = round(sum(speed)/len(speed),2)
    print("Average speed is "+ str(avg_speed)+ " miles per hour")
averageSpeed()







