# Torrent Player 2.25 — visible source sign-in pages

Fixed the embedded sign-in/registration window used by external sources including Electro-Torrent. Its floating activity used a wrap-content window with a zero-height weighted WebView. The window now receives bounded screen-relative dimensions at start, leaving a measured 897×307 px page area on the 960×540 TV fixture and 350×434 px on the 390×844 phone fixture.

Desktop-oriented account pages use a wide viewport with overview scaling and zoom support. On a trusted page, a bounded locator scrolls the site's own visible, same-origin password form into view; delayed DOM mounting is checked up to three times. It does not replace forms, read field values, submit credentials or click verification controls. Existing optional credential filling remains separate and runs only after the form is found. CAPTCHA, 2FA and email confirmation continue on the original website.

A Reload website button reopens the configured account URL. Main-frame network/HTTP errors now display a readable retry message. HTTPS certificate failures remain rejected. Navigation to same-origin form anchors is supported while the HTTP source policy still rejects fragment URLs; untrusted hosts, user-info URLs, non-HTTPS pages and local files remain blocked.

Live public-page probes found username/password forms on Electro-Torrent, Devil-Torrents, Best-Torrents, CinemaMovies and ExiTorrent. Chromium checks located visible password fields after the production locator ran at 960×360 and in mobile emulation at 390×480; the foreign-form fixture was rejected. No credentials were entered, no account created and no sign-in submitted. These checks verify form presentation, not authenticated account access or CAPTCHA completion.

Android 14 Robolectric tests cover bounded TV/phone windows and measured WebView allocation, all five configured account URLs, reload after a page error, form anchors and origin restrictions, and the original registration URL. Robolectric does not render native WebView frames, so page-area assertions use measured dimensions. Physical-device installation is not exercised here.
