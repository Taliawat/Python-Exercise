firstname = input("Enter your first name: ")
lastname = input("Enter your surname: ")

print("Hello " + firstname + " " + lastname)


#strings
word1 = "Good"
word2 = "Day"
word3 = "Tali"
 
#concatenating
sentence = word1 + " " + word2 + " " + word3
print (sentence)

#integers and floats
number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

float_number
print(number1)
print(number2)
print(round_number)

#Boolean
name = "Pep Guardogiola"
age = 3
bark = True
tweet = False

print("My pet is called", name, ", He is", age, "years old.")
print("Statement:", name, "barks.", bark)
print("Statement:", name, "tweets.", tweet)

#list
cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
cool_cows[2]
cool_cows[-1]
cool_cows[1:3]



#tuples
name = "Tali"

# we can assign the tuple values to variables as tuple lenght will not change
animals = "fox", "rabbit", "dog", "cat"
animal1, animal2, animal3, animal4 = animals

#returns rabbit
print(animal1)

#dicttionaries
noises = {"cow":"moo", "sheep":"baa", "Owen Wilson": "WoW"}
print(noises ["Owen Wilson"])

#adding to dictionary
noises["Big car man"] = "Vroom Vroom"
print(noises)

#overwriting
noises["sheep"] = "Speaks English"
print(noises)

print(list(noises.keys()))
print(list(noises.values()))
#returns tuples
print(list(noises.items()))

my_words = {"hello": "hola", "thank-you": "gracias"}
#getting values
print(my_words.get("hello"))

#pop used to remove specified key and return value
print(my_words.pop("thank-you)"))
print (my_words)

#updating
my_words.update({"yes":"ci"})
my_words.update({"yes":"sii"})
print (my_words)

########################################
#sets
my_items = ["Apple", "Banana", "Apple", "Banana", "Orange"]
set(my_items)


####################################
#Tutorial 

books = {"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}
print(books["The Handmaiden's Tale"])
# not possible as we are trying to print a value
print(books["Margaret Atwood"])
books.update({"Unfinished":"Priyanka Chopra Jonas","Unfinished":"Priyanka Chopra Jonas" })
#so
print(books.get("Margaret Atwood"))