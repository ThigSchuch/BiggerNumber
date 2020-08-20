import time

files = ["dataset-2-a.csv","dataset-2-b.csv","dataset-2-c.csv","dataset-2-d.csv","dataset-2-e.csv"]
saida = ["resposta-dataset-2-a.txt","resposta-dataset-2-b.txt","resposta-dataset-2-c.txt","resposta-dataset-2-d.txt","resposta-dataset-2-e.txt"]

def openFile(file):
    arq = open(file,"r")
    lines = arq.read().split("\n")
    arq.close()
    return lines

def appendFile(file, text):
    arq = open(file,"a")
    arq.write(text)
    arq.close()

for i in range(len(files)):
    start_time = time.time()
    bigger = 0
    lines = openFile(files[i])
    for number in lines:
        if int(number) > bigger:
            bigger = int(number)
            
    appendFile(saida[i], str(bigger)+"\n"+str(time.time() - start_time))