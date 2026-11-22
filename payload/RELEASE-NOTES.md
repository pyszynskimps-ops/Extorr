# Torrent Player 2.01 — Android TV and mobile preview

One application combines ExTorrent and 1337x with an extensible directory of 10 Polish and 10 international source profiles.

- Enable sources independently; add RSS/Atom/Torznab feeds or import declarative HTML/JSON rules.
- Progressive search, category batches of 120, positive-seed filtering and confirmed IMDb film/episode grouping.
- Saved sessions and personal API tokens are encrypted separately on the device. Website sign-in and assisted registration use original forms.
- Public torrents with identical hashes can share observed public trackers. Different releases remain separate.
- Before playback starts, failed metadata/buffering can try up to three confirmed alternative editions.
- English default and optional Polish. Existing subtitles, display modes, bookmarks and rolling buffer remain available.

TV: ARMv7 32-bit, package `pl.torrentplayer.tv`.
Mobile: ARM64 64-bit, package `pl.torrentplayer.mobile`.
Android 6.0 or newer; versionCode 201. These packages install separately from existing ExTorrent and 1337x apps.

Validation: 94 Android tests, 57 JVM check groups, local Chromium account-form tests, both APK builds, signatures, single-ABI/JNI gates and mobile 16 KB alignment checks passed. Native libraries reuse the SHA-256-verified 1337x 1.17 release; native engine sources are unchanged.

The directory does not mean every website is currently reachable or authenticated. Private sites require your account/invitation or personal API token. CAPTCHA, email confirmation, required website terms and payment require normal website interaction. No external accounts were created in tests. Published seeds do not guarantee a connection. Physical TV/phone playback and private logged-in catalogues still require device testing.

Preview/debug signing: keep the same signing key for updates. No existing standalone APKs or website download links are replaced.
