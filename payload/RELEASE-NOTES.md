# Torrent Player 2.06 — The Pirate Bay i YIFY/YTS

- Naprawiono pomijanie kategorii CAM/TS, filmów UHD/4K i seriali UHD/4K z The Pirate Bay.
- Zapisane pozycje TPB odzyskują dokładny torrent przez API szczegółów, także po opróżnieniu pamięci podręcznej. Odpowiedź dotycząca innego wydania jest odrzucana.
- Linki YIFY/YTS zachowują dokładny hash wydania, również przy zmianie domeny strony zwracanej przez API. Odtwarzanie takiego wydania nie wymaga odczytu nieznanej strony lustrzanej.
- Błąd API YTS jest odróżniany od poprawnego wyszukiwania bez wyników.

W kontrolach publicznych metadanych oba źródła zwróciły obie części Sicario (2015 i 2018). Parser odczytał wszystkie 302 wydania z dodatnimi seedami z czterech sprawdzonych odpowiedzi katalogu/wyszukiwania. Nie pobierano zawartości filmów. Liczba seedów zgłaszana przez serwis nie gwarantuje połączenia z konkretnego urządzenia.

Wersja testowa. TV: ARMv7 32-bit; mobile: ARM64 64-bit. Identyfikatory aplikacji i biblioteki silnika pozostają zgodne z 2.05. Podpisy APK są sprawdzane względem poprzedniego publicznego wydania.

Weryfikacja: 132 testy Androida, 59 grup testów JVM, obie kompilacje APK, kontrola pakietów/wersji/ABI/JNI/ikon/czcionek, podpisów i wyrównania mobile 16 KB zakończone poprawnie.
