numberOfTests = int(input("Enter Number of Test cases: "))
usernames=[[]*i for i in range(numberOfTests)]
names=[[]* i for i in range(numberOfTests)]

for j in range(numberOfTests):
    print("+++++++++++++ TEST CASE {} +++++++++++++".format(j + 1))
    numberOfTweets = int(input("Enter number of Tweeets for test case {} : ".format(j+1)))
    for i in range(numberOfTweets):
        usernames[j].append(input("{}. Enter space separated Username and Tweeet-id: ".format(i+1)))

for x in range(len(usernames)):
    names[x] = [n.split()[0] for n in usernames[x]]

column=0
for row in range(len(names)):
    if names[row].count(names[row][column])>1:
        result = sorted([[c,names[row].count(c)] for c in set(names[row]) if names[row].count(c)>1])
        print("\n".join(" ".join(map(str, line)) for line in result))
        column+=1