// a action
void quantity_to_pin(int pin, int quantity){
  analogWrite(pin,quantity);
}

void clear_pin(int pin){
  quantity_to_pin(pin,0);
}

// b action
void pins_loop(int pins[]){
  for (int i = 0; i < 3; i++){
    digitalWrite(pins[i],HIGH);
    delay(500);
    digitalWrite(pins[i],LOW);
  }
  digitalWrite(pins, HIGH);
  delay(500);
  digitalWrite(pins, LOW);
}

// send info
void sendint( float info){
  float i = info*5.0/1023.0;
  Serial.println(i);
  delay(100);
}

// r action
