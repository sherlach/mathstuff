problem = input("What is the inital word? Not case-sensitive.\n").upper()

letters = "".join(set(problem))
n = len(letters)
p = int(input("How long should the product-words be? Give as single numeral.\n"))

legalcharacters = {}

for letter in letters:
    legalcharacters[letter] = problem.count(letter)

def checklegality(term):
    for character in set(list(term)):
        if term.count(character) > legalcharacters[character]:
            return False
    return True

def cycle(delayfactor): #delayfactor changes the tempo - ie, a delayfactor of `n` means
                        #the iteration only progresses after n repetitions of the current step
    response=[]  
    while len(response) < p**n: #n**n before
        counterno = 0
        iteration = 1
        while counterno < n:
            
            response.append(letters[counterno])
            if iteration % delayfactor == 0:
                counterno += 1
            iteration += 1
    
    return response


answer=[]

for i in range(p**n):
    word=[]
    
    for k in range(p):
        word.append(cycle(n**k)[i])
       
    entry="".join(word)

    if checklegality(entry):
        answer.append(entry) 

print("Total number of valid words made:", str(len(answer)))
print(answer)

