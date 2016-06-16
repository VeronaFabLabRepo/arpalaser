


const char notaPin[9] = { 
  2,3,4,5,6,7,A2,A1,A0}; //Pin dei sensori in ingresso

void setup(){
  Serial.begin(9600);
  for(int i = 0; i < 9; i++){
    pinMode(notaPin[i],INPUT);
  }
}

void loop(){
  if(!digitalRead(notaPin[0])){ 
    Serial.println("0");
  }
  if(!digitalRead(notaPin[1])){ 
    Serial.println("1");
  }
  if(!digitalRead(notaPin[2])){ 
    Serial.println("2");
  }
  if(!digitalRead(notaPin[3])){ 
    Serial.println("3");
  }
  if(!digitalRead(notaPin[4])){ 
    Serial.println("4");
  }
  if(!digitalRead(notaPin[5])){ 
    Serial.println("5");
  }
  if(!digitalRead(notaPin[6])){ 
    Serial.println("6");
  }
  if(!digitalRead(notaPin[7])){ 
    Serial.println("7");
  }
  if(!digitalRead(notaPin[8])){ 
    Serial.println("8");
  }
  delay(500);
}










