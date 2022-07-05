s={18,"18",18.9}
print(s)           #{'18', 18,18.9}
print(len(s))      #3
s.add(20)
s.add("20")
s.add(20.0)     #if s.add(20.7) then print(len(s))=6
print(s)           #{18.9, 18, 20, '18', '20'}
print(len(s))      #5
s={}
print(type(s))    #<class 'dict'>
s=set()
print(type(s))    #<class 'set'>