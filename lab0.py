'''
myValue = False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

a = input('what is your name?')
print(a)
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(a,color,animal))


myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[-1])
myFruitList[2] = "orange"
print(myFruitList)


myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
print(myFinalAnswerTuple[-2])

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

myFavoriteFruitDictionary["Akua"] = "orange"
print(myFavoriteFruitDictionary)


myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
print(myMixedTypeList[2:5])

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))


from re import X


def double(a):
    y=a*2
    return y
print(double(5))

myFinalAnswerTuple = ["apple", "banana", "pineapple"]
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
def premierElementDeLaListe(a):
    b = a[2]  
    return b
print(premierElementDeLaListe(myMixedTypeList))
print(premierElementDeLaListe(myFinalAnswerTuple))

myFinalAnswerTuple = ["apple", "banana", "pineapple"]
for t in myFinalAnswerTuple:
    print(t.upper())

'''

