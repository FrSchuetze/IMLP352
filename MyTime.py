fin_E = open('data/english_list.csv',"r",encoding='UTF-8')
fin_M = open('data/math_list.csv',"r",encoding='UTF-8')
lisE=[]
lisM=[]
name=[]
for line in fin_E.readlines():
    #print(line, end='')
    line = line.strip().split(",")  #split by , make string into list
    #print(line, end='')
    name.append(line[0])
    lisE.append(line[1])
    
for line in fin_M.readlines():
    line = line.strip().split(",")
    lisM.append(line[1])
    
   
score=[]
fout = open("data/Score.csv","w")
line=''
for i in range(1,len(lisE)):
    score.append(int(lisE[i])+int(lisM[i]))
#    print(score)
    list1 = [name[i],str(score[i-1]),"\n"]
#    print(list1)
#    print(name[i],str(score[i-1]))
  
    line = ",".join(list1) #join all element in the stream by , and make it a string
#    print(line)

    fout.write(line)
fin_E.close()
fin_M.close()
fout.close()

line=''
fout = open("Score.csv","r")
#for line in fout.readlines():
#    print(line)

fout.close()
