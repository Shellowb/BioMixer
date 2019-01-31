/* calls the function that can acomplish the action*/
void perform_action(char action,int quantity){
  if (action == 'a'){
     quantity_to_pin(A0, quantity);
     delay(3000);
     clear_pin(A0);
  }
  else if (action == 'b'){
    //perform action b
    pins_loop(out_d_pins);
  }
  else if (action == 'c'){
    sendint((float)analogRead(A1));
  }
}

/* Determines the action and quantity that shoud be performed*/
void analize_input(String input){
  char action = input[0];
  String quantity = "";
  int i = 1;
  while( input[1] && input[i] != 'e' && i<10){
    quantity += input[i];
    i++;
  }
  //Serial.print("action "); Serial.println(action);
  //Serial.print("quantity "); Serial.println(quantity.toInt());
  perform_action(action,quantity.toInt());
}

/* Save Serial Entry as a String*/
void save_input(){
  while(Serial.available()){
    char i = (char)Serial.read();
    input += i;
    if( i == '\n'){
      saved_input = 1;
    }
  }
}

/* if there is an input this fuction will read it and call analize*/
void read_input(){
  if(saved_input){
    //Serial.print(input);
    analize_input(input);
    input = "";
    saved_input = 0;
  }
}  
