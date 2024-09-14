testString = "she walked the dog to the park and played ball with the dog When she threw the ball to the dog the dog missed the ball and ran to the other side of the park to fetch it"

dic = {}

words = testString.split()

for raw_word in words:
    word = raw_word.lower()
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

print (dic)