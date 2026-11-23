# Torrent Player 2.22 — napisy bez klucza API

- Usunięto SubDL, jego ustawienia i klucz z APK. Aktualizacja usuwa zapisane dane tego dostawcy z urządzenia.
- OpenSubtitles.org pozostaje pierwszym źródłem. Gdy nie ma dopasowania lub serwis jest niedostępny, aplikacja korzysta z publicznych stron YTS-Subs — bez API, konta i klucza.
- English i Polski dla filmów, z dokładnym dopasowaniem IMDb albo jednoznacznym tytułem i rokiem. Seriale nadal korzystają z OpenSubtitles.org; serwis zapasowy jest katalogiem filmowym.
- SRT jest obsługiwany bezpośrednio; polskie napisy MPL2 są przeliczane na SRT bez zgadywania liczby klatek. Pobrane napisy zachowują pozycję i stan pauzy oraz są czyszczone po odtwarzaniu.
- Zachowano doładowywanie filmów na końcu listy i zabezpieczenia zmiany wydania z 2.21.

Sprawdzenie rzeczywistego klienta: angielski plik do Sicario (2015), 989 wpisów; polski plik MPL2 do Spectre (2015), 955 wpisów po konwersji do SRT. Wyszukiwanie HTML po tytule i roku również przeszło test. Dostępność języków zależy od filmu i dostawcy.

228 testów Androida przeszło bez błędów (114 TV, 114 mobile). Sprawdzone podpisy aktualizacji, architektury, zasoby i wyrównanie 16 KB dla mobile. TV: ARMv7, 32-bit; mobile: ARM64, 64-bit. Android 6 lub nowszy. Wersja testowa z dotychczasowym podpisem debug. Nie przeprowadzono instalacji na fizycznym TV/telefonie.
