# Torrent Player 2.23 — alternative subtitle verification

Fixed a download failure on movies with many subtitle uploads, reproduced live with Inception (2010), English. The catalogue displayed the first 40 results but stored identity proofs for every upload; later uploads evicted proofs for the visible rows. Identity proofs are now registered only for the returned results. Existing identity, language, archive and URL checks remain active. A regression test downloads every displayed result from a 220-upload fixture.

Title/year search without an IMDb hint also returned the correct Sicario, The Matrix and Inception pages.

The production YTS-Subs client was exercised anonymously on six films, in English and Polish: Sicario (2015), Spectre (2015), The Matrix (1999), Inception (2010), Interstellar (2014), Arrival (2016). Eleven combinations returned downloadable subtitle files after the fix. Sicario had no Polish upload on this provider; this is reported as unavailable rather than substituted with another language or film. Public HTML and ZIP links only; no account or API key is required.

Downloaded files are verified through Media3's actual SubRip parser and the subtitle-controller fallback flow on Android 14 Robolectric, for both TV and mobile. Checks cover cue timing, selected text track, language, retained video URI, position and playing/paused state, and cache cleanup. Recorded public website responses make the UI attachment test repeatable without requiring network calls during Robolectric execution. Dialogue and ZIP files remain local and are not included in the source repository or APK.

This verifies downloading, parsing and player attachment. Visual synchronization against a particular movie release and playback on a physical TV are not verified here; choose subtitles matching the video's release. OpenSubtitles.org remains primary and YTS-Subs is the film-only backup.
