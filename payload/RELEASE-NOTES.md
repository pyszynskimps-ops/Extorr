# Torrent Player 2.05 — języki wydań, angielskie tytuły i płynniejsze przeglądanie

- W języku English tytuły filmów są lokalizowane w katalogu, panelu „In the spotlight”, karcie filmu, wyborze wydania, zarządzaniu ulubionymi i oknie przygotowania odtwarzania.
- Pierwszeństwo mają dokładnie dopasowane tytuły z metadanych. Pozostałe polskie nazwy są tłumaczone w tle; opisy nadal korzystają z tłumaczenia na angielski. Rozpoznawanie języka chroni nazwy takie jak „Sicario” przed niepotrzebnym dosłownym tłumaczeniem.
- Dodano czytelny rok produkcji jako etykietę na plakacie. Nieznany rok jest ukrywany.
- Uzupełniono angielską nazwę języka polskiego i etykiety ścieżek napisów. Kompletność kluczy tekstów interfejsu jest sprawdzana przy generowaniu aplikacji.
- Tłumaczenia mają ograniczoną kolejkę, pamięć podręczną i ochronę przed spóźnionymi odpowiedziami po przewinięciu lub zmianie języka. W razie niedostępności usługi pojawia się komunikat po angielsku.

- Dodano języki audio i napisów na miniaturkach, karcie filmu oraz liście wydań. MULTI bez szczegółów nie jest traktowane jako potwierdzenie konkretnego języka.
- Plakaty współdzielą pobieranie; kolejki i liczba zadań są ograniczone. Odświeżenia listy są łączone, a doładowywanie w tle ustępuje przewijaniu i wybranej kategorii.
- Pasek przewijania jest grubszy, kontrastowy i nie zanika.
- Publiczne magnety otrzymują zapasowe trackery UDP/HTTPS. Prywatne torrenty i trackery z danymi dostępu pozostają zachowane.
- Naprawiono budowanie listy alternatywnych wydań po dokładnym dopasowaniu IMDb. Po 45 sekundach całkowitego braku połączeń można spróbować innego dokładnie pasującego wydania; działające pobieranie i rozpoczęte odtwarzanie są zachowane.

Oryginalne dane wydań pozostają do wyszukiwania, rozpoznawania filmu, napisów i zapisu pozycji odtwarzania. Nazwy własne serwisów, nazwiska, nazwy plików i oryginalne strony logowania/CAPTCHA zachowują swoją treść.

TV: ARMv7 32-bit, pl.torrentplayer.tv. Mobile: ARM64 64-bit, pl.torrentplayer.mobile. VersionCode 205 / versionName 2.05.

Walidacja lokalna: 132 testy Androida (66 na wariant), 59 grup testów JVM, oba APK, kontrolne testy trackerów TCP/HTTPS, kontrola pakietów, ABI, JNI, podpisów, czcionek oraz wyrównania mobile 16 KB. Podpisy zgodne z publiczną wersją 2.04. Testy wykorzystują dane i swarm kontrolny; nie potwierdzają jeszcze działania konkretnego filmu w sieci użytkownika.
