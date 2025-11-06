const int soundPin = A0;
const int ledPin = 9;
const int threshold = 600;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Sound Detection Ready");
}

void loop() {
  int value = analogRead(soundPin);
  Serial.print("Sound Level: ");
  Serial.println(value);

  if (value > threshold) {
    digitalWrite(ledPin, HIGH);
    delay(200);
  } else {
    digitalWrite(ledPin, LOW);
  }

  delay(100);
}

