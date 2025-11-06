const int buzzer = 8;
const int ledDry = 9;
const int ledHumid = 10;
const int ledWet = 11;

void setup() {
  pinMode(A0, INPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(ledDry, OUTPUT);
  pinMode(ledHumid, OUTPUT);
  pinMode(ledWet, OUTPUT);

  Serial.begin(9600);
  Serial.println("Soil Moisture Monitoring Ready");
}

void loop() {
  int sensorValue = analogRead(A0);

  digitalWrite(ledDry, LOW);
  digitalWrite(ledHumid, LOW);
  digitalWrite(ledWet, LOW);
  noTone(buzzer);

  if (sensorValue >= 1000) {
    Serial.println("Not in soil or disconnected");
  } 
  else if (sensorValue >= 600) {
    Serial.println("DRY SOIL");
    digitalWrite(ledDry, HIGH);
    tone(buzzer, 1000);
    delay(1000);
    noTone(buzzer);
  } 
  else if (sensorValue >= 370) {
    Serial.println("HUMID SOIL");
    digitalWrite(ledHumid, HIGH);
  } 
  else {
    Serial.println("WATER SOIL");
    digitalWrite(ledWet, HIGH);
  }

  Serial.println("----------");
  delay(2000);
}

