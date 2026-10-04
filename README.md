# mis203-basic-programming

## Week 02

## AI Tool Used:
Gemini
### Prompt Used: Temel bir not hesaplama programı yazmam gerekiyor. while True ile döngü kurup kullanıcıdan isim almalı, isim 'q' girilirse break ile çıkmalı. Sonra score istemeli; score 0-100 arasında değilse uyarı verip continue ile tekrar sormalı. 90-100 A, 80-89 B, 70-79 C, 60-69 D, 0-59 F harf notunu ekrana 'Ali: 85 -> B' formatında basıyor olmalı. Döngü bitince de total students ve average score'u 2 decimal places ile hesaplamalı, hiç öğrenci girilmediyse 'No students entered.' demeli. Pythona yeni başlayan birinin anlayacağı sadelikte temel Python ile kodu yaz.
### What did you change?: I simplified the variable names to make them easier to track and added an integer check so whole numbers don't show unnecessary decimals.
- **What does break do in your program?:** In this program, break stops the while loop when the user enters "q" so the program can show the final average score.


## Week 03

- **AI Tool Used:** Gemini
- **Prompt Used:** Bana temel seviyede Python ile çalışan bir sinema bileti gişe programı yaz. while True döngüsü olsun, q ile çıkılsın. Yaş 0-120 arası değilse veya gün yanlış girilirse continue ile başa dönsün. if/elif ile yaş ve öğrenci durumuna göre indirimleri sırayla hesaplasın. Lütfen yeni başlayan birinin anlayacağı basitlikte yaz.
- **What did you change?:** I changed the math for the discounts. Instead of finding the discount amount and subtracting it, I just multiplied the price by the remaining percentage to keep it simple.
- **Tests:** 
  1. Age 6 (boundary), weekday, no -> Child, 120.00 TRY
  2. Age 22, weekend, yes -> Student, 175.00 TRY
  3. Age 70, weekday, no -> Senior, 100.00 TRY
- **Why does the order of the rules matter?:** Python checks the rules from top to bottom. If we put the "Student" rule before the "Child" rule, a 10-year-old student will get the 30% student discount instead of their 40% child discount.
