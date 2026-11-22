# Torrent Player 2.08 — napisy wbudowane i OpenSubtitles.org

Menu napisów zawiera opcję wyłączenia, rzeczywiste ścieżki filmu i dwa przyciski pobierania z OpenSubtitles.org: English oraz Polski. Usunięto tryb automatyczny, dodatkowy skrót English, informację o niedostępnej angielskiej ścieżce i ustawienia klucza API z menu napisów.

Pobieranie używa strony opensubtitles.org/pl i jej publicznych wyników XML. Nie wymaga klucza API OpenSubtitles.com. Wybór wydania uwzględnia język, tożsamość filmu, rok lub sezon i odcinek. Pliki SRT i archiwa ZIP są sprawdzane przed włączeniem; pobrane napisy nie zmieniają pozycji filmu ani stanu pauzy. Przełączenie na napisy wbudowane lub wyłączenie napisów anuluje wcześniejsze pobieranie.

Sprawdzono publiczne wyniki polskie i angielskie oraz poprawne archiwa obu języków. Dostępność konkretnego wydania i limity pobierania zależą od OpenSubtitles.org.

TV: ARMv7 32-bit. Mobile: ARM64 64-bit. Wydanie testowe; zgodność podpisu aktualizacji sprawdzana względem 2.07.

Weryfikacja: 134 testy Androida (67 na wariant), 60 grup testów JVM, sprawdzenie rzeczywistych XML/ZIP oraz pobieranie napisów obu języków nowym klientem HTTPS. Oba APK przeszły kontrolę pakietów/wersji/ABI/JNI/ikon/czcionek/podpisów oraz wyrównania mobile 16 KB.
