#define sensorPin A3

int dryLimit = 1000;
int wetLimit = 300;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int data = analogRead(sensorPin);

  int percent = map(data, dryLimit, wetLimit, 0, 100);
  percent = constrain(percent, 0, 100);
  Serial.println(percent);
  delay(1000);

}
