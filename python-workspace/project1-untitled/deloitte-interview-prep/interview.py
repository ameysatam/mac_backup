# mystring = "Hello"
# mylist =[letter for letter in mystring]
# print(mylist)
#
# list2 = [1,2,3,4,5,6,67]
# lists3 = [x for x in list2 if x%2==0]
# print(lists3)
#
# celcius = [0,12,100,-5]
# fahrenheit = [((9/5)*temp + 32) for temp in celcius]
# print(fahrenheit)

divisibleBy8 = [i for i in range(1,1000) if i%8==0]
print(divisibleBy8)

haveSixInThem = [num for num in range(1,1000) if "6" in str(num)]
print(haveSixInThem)

string_1 = "Practice Problems to Drill List Comprehension in Your Head."
q3_answer = len([characters for characters in string_1 if characters==" "])
print(q3_answer)

q4_answer = "".join([characters for characters in string_1 if characters not in "aeiou"])
print(q4_answer)

words = string_1.split(" ")
q5_answer = len([characters for characters in words if len(characters)<5])
print(q5_answer)

q6_answer = {word:len(word) for word in words}
print(q6_answer)