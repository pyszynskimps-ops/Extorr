# Torrent Player, ExTorrent i 1337x — pobieranie APK

Publiczne pliki instalacyjne do podlinkowania na stronie. Pobieranie nie wymaga logowania do GitHuba.

| Aplikacja | Android TV — ARMv7, 32-bit | Android mobile — ARM64, 64-bit |
|---|---|---|
| Torrent Player 2.21 | [torrent-player-android-tv-armeabi-v7a.apk](https://github.com/pyszynskimps-ops/Extorr/releases/download/torrent-player-v2.21/torrent-player-android-tv-armeabi-v7a.apk) | [torrent-player-android-mobile-arm64-v8a.apk](https://github.com/pyszynskimps-ops/Extorr/releases/download/torrent-player-v2.21/torrent-player-android-mobile-arm64-v8a.apk) |
| ExTorrent / Extor 1.04 | [extor-android-tv-armeabi-v7a.apk](https://github.com/pyszynskimps-ops/Extorr/releases/download/extor-v1.04/extor-android-tv-armeabi-v7a.apk) | [extor-android-mobile-arm64-v8a.apk](https://github.com/pyszynskimps-ops/Extorr/releases/download/extor-v1.04/extor-android-mobile-arm64-v8a.apk) |
| 1337x 1.17 | [1337x-android-tv-armeabi-v7a.apk](https://github.com/pyszynskimps-ops/Extorr/releases/download/1337x-v1.17/1337x-android-tv-armeabi-v7a.apk) | [1337x-android-mobile-arm64-v8a.apk](https://github.com/pyszynskimps-ops/Extorr/releases/download/1337x-v1.17/1337x-android-mobile-arm64-v8a.apk) |

[Wydania i sumy SHA-256](https://github.com/pyszynskimps-ops/Extorr/releases). Każde wydanie zawiera dwa APK oraz plik SHA256SUMS.

Dla strony: [downloads.json](https://raw.githubusercontent.com/pyszynskimps-ops/Extorr/main/downloads.json) zawiera aktualne wersje, bezpośrednie linki, architektury, rozmiary plików i sumy SHA-256.

To kompilacje testowe z podpisem debug. Certyfikat może różnić się od wcześniejszych wydań; wtedy Android odrzuci instalację jako aktualizację. Odinstalowanie poprzedniej aplikacji usuwa jej lokalne dane.

1337x 1.17 tłumaczy opisy na angielski przy języku English. ExTorrent / Extor zachowuje polski interfejs. Dostępność napisów zależy od tytułu i języka.

Torrent Player 2.21 to osobna aplikacja łącząca ExTorrent i 1337x, z katalogiem 20 profili źródeł i możliwością dodawania RSS/Atom/Torznab oraz reguł HTML/JSON. Domyślny język: angielski, dostępny też polski. Prywatne serwisy wymagają własnego konta lub tokenu; CAPTCHA i potwierdzenie e-mail wykonuje użytkownik w formularzu serwisu. Liczba seedów nie gwarantuje połączenia. Wersja testowa wymaga sprawdzenia na urządzeniu.

Cinema Copper 2.02 wprowadza grafitowe tło, miedziane akcenty, czcionki Manrope i DM Serif Display oraz górne menu. Podpis APK jest zgodny z publicznym wydaniem Torrent Player 2.01.

Wersja 2.03 przenosi statusy stron, logowania i weryfikacji do Settings → Options. Ustawienia nie pokazują kategorii ani licznika filmów. Usunięto wskazane dodatkowe kategorie i poprawiono widoczność etykiet oraz opisów opcji. Podpisy APK są zgodne z publiczną wersją 2.02.

Wersja 2.04 zmniejsza panel „In the spotlight”, rezerwuje miejsce na pełny rząd kart oraz poprawia układ karty filmu i przycisku logowania w Settings. Podpisy APK są zgodne z wersją 2.03.

Wersja 2.05 dodaje angielskie tytuły, rok produkcji i języki wydań na plakatach, wyraźniejszy pasek przewijania oraz ograniczone kolejki pobierania w tle. Naprawia blokowanie nowej kategorii przez poprzednie żądanie i wybór dokładnie pasujących wydań do ponownej próby. Publiczne magnety otrzymują zapasowe trackery UDP/HTTPS; dostępność konkretnego filmu zależy od rzeczywistych peerów. Podpisy APK są zgodne z wersją 2.04.

Wersja 2.06 naprawia brakujące kategorie UHD/4K i CAM/TS z The Pirate Bay oraz odzyskiwanie dokładnego źródła TPB i YIFY/YTS po utracie rekordu z pamięci podręcznej. Rozróżnia błąd API YTS od braku wyników. Oba źródła zwróciły obie części Sicario w sprawdzonych odpowiedziach API; rzeczywiste połączenie zależy od dostępności peerów. Przeszły 132 testy Androida i 59 grup testów logiki. Podpisy i biblioteki silnika są zgodne z 2.05.

Wersja 2.07 dopasowuje całe plakaty do ramek katalogu i panelu „In the spotlight”, zachowując proporcje i wyśrodkowanie bez przycinania. Przeszło 14 testów układu TV/mobile i weryfikacja obu APK. Podpisy aktualizacji i biblioteki silnika są zgodne z 2.06.

Wersja 2.08 upraszcza menu napisów do rzeczywistych ścieżek odtwarzacza, wyłączenia i pobierania English/Polski z OpenSubtitles.org. Usuwa dodatkowy skrót English, tryb automatyczny i ustawienia klucza API z tego menu. Wyszukiwanie i pobieranie korzystają z publicznych wyników XML i archiwów ZIP/SRT serwisu. Przeszły 134 testy Androida i 60 grup testów logiki oraz rzeczywiste pobieranie obu języków. Podpisy aktualizacji i biblioteki silnika są zgodne z 2.07.

Wersja 2.09 usuwa duplikaty kart na podstawie dokładnej tożsamości filmu/odcinka, wybiera więcej seedów i wyższą rozdzielczość przy remisie oraz udostępnia kategorie bez ExTorrent. Home pokazuje filmy z bieżącego roku, po 120 różnych pozycji i kolejne partie po przewinięciu. Przeszło 136 testów Androida i 61 grup testów logiki. [Strona aplikacji](https://moja-witryna-624a5d.glovedpaint5.chatgpt.site) zawiera główny Torrent Player, szerszy opis i zrzuty interfejsu. Podpisy i biblioteki silnika są zgodne z 2.08.

Wersja 2.20 dodaje zapasowe pobieranie napisów z SubDL po braku wyników OpenSubtitles, z gotową konfiguracją zachowywaną po restarcie i wylogowaniu z katalogów. Udostępnienie wspólnej konfiguracji SubDL w publicznych APK zostało zatwierdzone przez właściciela klucza. Klucz jest możliwy do odczytania z APK, a jego limit jest współdzielony; nie ma go w kodzie źródłowym ani treści strony. Własny zapisany klucz użytkownika ma pierwszeństwo. Dostępność napisów i limity zależą od dostawcy.

Wydanie obejmuje też poprawki przeglądania pilotem, ograniczenie zadań metadanych i plakatów w tle, dokładne dopasowanie opisów IMDb, przewijanie długich opisów i tłumaczenie na polski. Z karty filmu usunięto wiersz Audio; ustawienia ścieżek odtwarzacza pozostają dostępne. Testy: 226 testów Androida (113 TV, 113 mobile), bez błędów. Zachowano zgodność podpisów z publicznym 2.09 i mobile ARM64 z wyrównaniem 16 KB. Nie przeprowadzono instalacji na fizycznym TV/telefonie.

Niski bufor: odtwarzanie pobiera jeden plik o stałej jakości. Ta wersja nie zmienia automatycznie rozdzielczości podczas odtwarzania. Mniejsze wydanie tego samego filmu może wymagać mniejszego pasma, ale jego uruchomienie wymaga ponownego buforowania.

Wersja 2.21 dopisuje doładowane filmy na końcu katalogów i wyników wyszukiwania bez przestawiania wcześniejszych kart. Home zachowuje poprzednie partie po 120 pozycji, a ręczna zmiana sortowania porządkuje całą listę. Zabezpieczono przełączanie wydań po zamknięciu okna Release i anulowanie oczekującej zmiany po cofnięciu. Przeszło 238 testów Androida (119 TV i 119 mobile), bez błędów. Zgłoszonej awarii fizycznego TV nie odtworzono w środowisku testowym. Podpisy i biblioteki silnika są zgodne z 2.20; wspólna konfiguracja SubDL została zachowana.
