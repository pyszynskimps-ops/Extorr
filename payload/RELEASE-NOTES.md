# Torrent Player 2.21 — Cinema Copper

- Doładowane filmy trafiają na koniec katalogu i wyników wyszukiwania. Wcześniejsze pozycje zachowują kolejność, a nowe są porządkowane według wybranego sortowania.
- Home zachowuje poprzednie partie przy doładowaniu 120 → 240 → 300 i kolejnych filmów. Lepsze wydanie zastępuje kartę tego samego filmu na jej miejscu.
- Ręczna zmiana sortowania porządkuje całą listę.
- Zabezpieczono zmianę wydania w „Release”: karta otwiera się po zamknięciu okna wyboru, cofnięcie anuluje oczekującą zmianę, a nieaktualne wywołania nie podmieniają innej strony. Błąd otwierania wydania pokazuje komunikat i wraca do katalogu.
- Zachowano dotychczasową konfigurację SubDL, napisy English / Polski i zgodność podpisu aktualizacji z wersją 2.20.

Android TV: ARMv7, 32-bit. Android mobile: ARM64, 64-bit, wyrównanie 16 KB. Android 6 lub nowszy; English / Polski. Wersja testowa z dotychczasowym podpisem debug.

Weryfikacja: 238 testów Androida, zero błędów (119 TV, 119 mobile), w tym doładowanie rzeczywistych list i wielokrotne przełączanie dwóch wydań w obu językach. Awarii zgłoszonej na fizycznym telewizorze nie odtworzono w środowisku testowym; zabezpieczenie wymaga jeszcze potwierdzenia na tym urządzeniu. Nie przeprowadzono instalacji na fizycznym TV/telefonie.

Publiczne APK zawierają wcześniej zatwierdzoną wspólną konfigurację SubDL. Klucz jest możliwy do odczytania z APK, a limit usługi współdzielony. Nie ma go w kodzie źródłowym, treści strony ani logach. Dostępność napisów zależy od dostawcy.
