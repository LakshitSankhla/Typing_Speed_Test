import time
import random

def get_sentences():
    filename = 'typing_speed_test.txt'
    fh = open(filename)

    #appending lines
    msg = []
    for line in fh:
        for word in line.split('. '):
            msg.append(word)

    return msg

def test(msg):
    n = random.randint(0,len(msg)-1)        #randomly selecting a line from above file
    string = msg[n]
    print(string)
    l = len(string)
    print("Enter the above text and press Enter in: ")
    print(3, end=' ')
    time.sleep(1)
    print(2, end=' ')
    time.sleep(1)
    print(1, end=' ')
    time.sleep(1)
    print('Now:')
    start_time = time.time()        #Start Time
    result = str(input())
    stop_time = time.time()           #Stop Time

    total_time = stop_time - start_time
    count = 1
    for i,c in enumerate(string):
        try:
            if result[i] == c:
                    count += 1
        except:
            pass

    accuracy = count / l * 100
    return total_time , accuracy

if __name__ == "__main__":

    lines = get_sentences()
    total_time , accuracy = test(lines)

    print("Time Taken= %f "% total_time)
    print("Accuracy= %f" % accuracy)


