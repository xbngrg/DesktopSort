#t_textRead2.py
tagList = []
tagFile = open('Tests/tagfile3.txt','r')
for tagLine in tagFile:
    tagLine = tagFile.readlines()
    print(tagLine)
    tagList.append(tagLine)
    print(tagList)



