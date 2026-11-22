# Torrent Player 2.02 — Cinema Copper

The approved Cinema Copper design is implemented in the native Android TV and mobile app.

- Warm matte graphite, ivory text and copper actions/focus, including dialogs and launcher artwork.
- Bundled Manrope and DM Serif Display fonts with Polish characters; fonts work offline on Android 6+.
- Top navigation and horizontal categories replace the sidebar. Home features the selected film above a compact catalogue.
- Film cards show a portrait poster, fitted description, rating, seeds, release/favourites and equally sized play/back actions.
- Portrait phones use a stacked card. Compact landscape layouts reserve more room for browsing.
- Preparation appears in a smaller themed dialog with actual engine status and indeterminate progress; no fabricated rates or percentages.

TV: ARMv7 32-bit, `pl.torrentplayer.tv`.
Mobile: ARM64 64-bit, `pl.torrentplayer.mobile`.
Version 2.02 / versionCode 202; Android 6.0 or newer.

Validation: 106 Android tests, 57 JVM check groups, both APK builds, bundled-font and test-data-exclusion checks, signatures, package/ABI/JNI checks and mobile 16 KB alignment passed. Native engine sources are unchanged; libraries reuse the SHA-256-verified 1337x 1.17 release. The APK signing certificate matches the public Torrent Player 2.01 APKs, allowing an in-place update from that release.

This is a preview/debug release. Android render tests use fixture metadata; the screenshots/preview and sample catalogue are excluded from the APK. Real playback on a physical TV/phone still requires device testing.

The existing source directory, source access requirements and native player remain in use. Private websites require your own account/token and normal website verification. Old standalone ExTorrent/1337x download links remain available.
