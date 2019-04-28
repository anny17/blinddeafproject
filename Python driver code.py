import time
import serial                                 
ardser = serial.Serial('com3',9600)  
print(ardser.readline())              
print("Enter the string to output in braille")
def string1(ch):
      ch=ch.lower()
      arr={'a':'100000','b':'110000','c':'100100','d':'100110','e':'100010','f':'110100','g':'110110','h':'110010','i':'010100','j':'010110','k':'101000','l':'111000','m':'101100','n':'101110','o':'101010','p':'111100','q':'111110','r':'111010','s':'011100','t':'011110','u':'101001','v':'111001','w':'010111','x':'101101','y':'101111','z':'101011',' ':'000000'}   
      return arr[ch]
while 1:                              
    input_data = input()              
    print("you entered", input_data)  
    str1=""
    for i in range(0,len(input_data)):
        str1=string1(input_data[i])
        for j in range(1,len(str1)+1):
            if (str1[j-1] == '1'):    
                ardser.write(str(j).encode('ASCII'))
                #print ("LED ON")
            #else:                   #if the entered data is 0
             #   ardser.write('0'.encode('ASCII'))             #send 0 to arduino 
                #print ("LED OFF")
            
        time.sleep(1)
        ardser.write('0'.encode('ASCII'))
ardser.close()
