# Write your code here.
# test change

def hello():
    return "Hello!"

def greet(name):
    return f"Hello, {name}!"


def calc(num1,num2,op="multiply"):
    match op:
        
        case "add":
            return num1+num2
        case "multiply":
            try:
                total = num1*num2
            except Exception:
                return "You can't multiply those values!"
            else:
                return total
        case "divide":
            try:
                total = num1/num2
            except Exception:
                return "You can't divide by 0!"
            else:
                return total
        case "subtract":
            return num1-num2
        case "modulo":
            return num1%num2

def data_type_conversion(val,type):
    match type:
        case "int":
            try:
                new_val= int(val)
            except Exception:
                return f"You can't convert {val} into a int."
            else:
                return new_val
        case "float":
            try:
                result = float(val)
            except Exception:
                return f"You can't convert {val} into a {type}"
            else:
                return result
        case "str":
            try:
                result = str(val)
            except Exception as e:
                return e
            else:
                return result

def grade(*args):
    try:
        grade = sum(args)/len(args)
    except Exception:
        return "Invalid data was provided."
    if grade >= 90:
        return 'A'
    elif grade >= 80 and grade<=89:
        return 'B'
    elif grade >=80 and grade<=89:
        return 'B'
    elif grade>=70 and grade<=79:
        return 'B'
    elif grade>=60 and grade<=69:
        return 'B'
    else:
        return 'F'
    
def repeat(word,count):
    full = ""
    for i in range(count):
        full = full+word
    return full

def student_scores(type, **kwargs):
    
    if type == "best":
        max = 0
        person =""
        for key,val in kwargs.items():
            if max<val:
                max = val
                person = key
        return person
    elif type == "mean":
        total = sum(list(kwargs.values()))/len(list(kwargs.values()))
        return total

def titleize(oldTitle):
    words = oldTitle.split(" ")
    for i in range(len(words)):
        if i == 0:
            words[i] = words[i].capitalize()
        elif i == len(words)-1:
            words[i] = words[i].capitalize()
        else:
            if len(words[i]) >3:
                words[i] = words[i].capitalize()
    newTitle = " ".join(words)
    return newTitle

def hangman(secret,guess):
    revealed = ""
    counter = 0
    for i in range(len(secret)):
        while counter < len(guess):

            if guess[counter] == secret[i]:
                revealed += guess[counter]
                counter = 0
                break
        
            counter+=1
        else:
            revealed +="_"
            counter = 0
    return revealed

def pig_latin(word):
    VOWELS = "aeiou"
    listified = list(word)
    if word[0] in VOWELS:
        word+="ay"
        return word
    elif word[0] not in VOWELS:
        while word[0] not in VOWELS:
            constonant = listified.pop(0)
            listified.append(constonant)
        listified.append("ay")
        return  "".join(listified)
    elif listified[0,1] == "qu":
        listified.pop(0)
        listified.pop(0)
        listified.append("qu")
        return "".join(listified)
    
        
        