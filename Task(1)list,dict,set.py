#list
Reg_No=[10,20,30,40,50]
Reg_No.append(60)
Reg_No.remove(30)
Reg_No[0]=5
print("Updated List:",Reg_No)


#dict
data={"Name":"Sanmu","Age":21,"city":"Coimbatore"}
data["Gender"]="Female"
del data["Age"]
data["city"]="Mumbai"
print("Updated Dictonary:",data)


#set
n={2,4,6,8}
n.add(10)
n.remove(6)
n.discard(2)
n.add(12)
print("Update set:",n)

