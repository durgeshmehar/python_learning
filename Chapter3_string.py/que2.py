letter='''Dear <|name|>,
    you are selected!
    <|date|>'''
name=input("Enter the name\n")
date=input("Enter date dd\mm\yyyy\n")

letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)