import sys

spam = [21,22]
#spam = ['apples', 'bananas', 'tofu', 'cats']
#spam = [1,2,3,["tofu",3]]

# result should be 'apples, bananas, tofu, and cats'

def separateListItems(inputList):
    # prvo, trebo bih testirat na to je li lista prazna
    if len(inputList) == 0:
        print("You provided an empty list. Please provide a proper list containing items")
        sys.exit()
    elif len(inputList)==1:
        print(inputList[0])
    else:
        stringList = str()
        for i in range(len(inputList)):
            if i < (len(inputList)-2):
                stringList+=str((inputList[i]))
                stringList+=", "
            elif i < (len(inputList)-1):
                stringList+=str((inputList[i]))
            else:
                stringList+=", and "
                stringList+=str((inputList[i]))
            
    print(stringList)

separateListItems(spam)

def comma_code(items):
    items = [str(item) for item in items]
    if not items:
        return ''
    if len(items) == 1:
        return items[0]
    return ', '.join(items[:-1]) + ', and ' + items[-1]

result = comma_code(spam)
print(result)

