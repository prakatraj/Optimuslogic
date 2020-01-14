import string
text=open("a.txt","r")
d=dict()
num_words=0
for line in text:
    line=line.strip()
    line=line.lower()
    line=line.translate(line.maketrans("","",string.punctuation))
    words=line.split(" ")
    num_words =len(words)
    print("Number of words:")
    print(num_words)
    for word in words:
        if word in d:
            d[word]=d[word]+1
        else:
             d[word]=1
for key in list(d.keys()):
    print(key, ":",d[key])