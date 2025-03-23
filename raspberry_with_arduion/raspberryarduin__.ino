void setup() {
  // put your setup code here, to run once:
  pinMode(A0,INPUT);
  Serial.begin(9600);
}
int data=0;

void loop() {
  // put your main code here, to run repeatedly:
  data = map(analogRead(A0),0,1024,1,255);
  if(Serial.available()){
    if('s'==Serial.read()){
      Serial.print(data);
    }
  }
  delay(10);
}
