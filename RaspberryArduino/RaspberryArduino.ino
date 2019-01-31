String  input       = "";
bool    saved_input = 0;
int out_d_pins[] = {2,3,5};
int out_a_pins[] = {A0};
int in_a_pins[] = {A1};

void setup (){
  Serial.begin(9600);
  pinMode(out_d_pins,OUTPUT);
  pinMode(out_a_pins,OUTPUT);
  pinMode(in_a_pins,INPUT);  
}

void loop(){
 save_input();
 read_input();
}
