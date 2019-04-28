const int led=10;
int value=0;

void setup() 
   { 
      Serial.begin(9600); 
      pinMode(12, OUTPUT);
      pinMode(10, OUTPUT);
      pinMode(8, OUTPUT);
      pinMode(6, OUTPUT);
      pinMode(4, OUTPUT);
      pinMode(2, OUTPUT);
      digitalWrite (12, LOW);
      digitalWrite(10,LOW);
      digitalWrite(8,LOW);
      digitalWrite(6,LOW);
      digitalWrite(4,LOW);
      digitalWrite(2,LOW);
      Serial.println("Connection established...");
   }
 
void loop() 
   {
     while (Serial.available())
        {
           value = Serial.read();
        }
     
     if (value == '1')
     {
      digitalWrite(12,HIGH);
     }
     else if (value == '2')
     {
      digitalWrite(10,HIGH);
     }
     else if (value == '3')
     {
      digitalWrite(8,HIGH);
     }
     else if (value == '4')
     {
      digitalWrite(6,HIGH);
     }
     else if (value == '5')
     {
      digitalWrite(4,HIGH);
     }
     else if (value == '6')
     {
      digitalWrite(2,HIGH);
     }
     else if (value == '0')
     {
      digitalWrite(12,LOW);
      digitalWrite(10,LOW);
      digitalWrite(8,LOW);
      digitalWrite(6,LOW);
      digitalWrite(4,LOW);
      digitalWrite(2,LOW);
     }
   }
