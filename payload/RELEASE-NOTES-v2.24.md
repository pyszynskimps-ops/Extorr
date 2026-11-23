# Torrent Player 2.24 — Home posters and independent language preferences

Home / All films now uses the same TV grid as the remaining catalogues: five columns and cards up to 280 dp tall, reduced consistently when the available viewport is shorter. The common panel reserves space for a complete row, reducing or hiding the optional spotlight when necessary. Mobile retains its existing common responsive grid and card sizing. Artwork remains fitted without cropping.

Subtitle menus and external-subtitle progress/result dialogs use a context configured from the saved application-language preference, independently of the selected subtitle language and device locale. Playback restores the saved UI language at activity creation and uses the same localized context for Media3 controls.

Changing embedded subtitles, turning subtitles off or attaching an external SRT preserves the currently selected audio track. If audio selection was automatic, the current supported track is pinned and its language retained before changing text parameters/re-preparing the media item. An explicit audio override, disabled audio and other playback preferences are preserved. Downloaded subtitles retain video URI, position and paused/playing state.

Android 14 regression coverage checks Home/catalogue card dimensions, complete rows on short TV layouts, an English interface with Polish embedded subtitles, a Polish interface with English downloaded subtitles, device/UI locale differences, selected audio and existing explicit audio overrides. Verification uses Robolectric and player test doubles; physical TV playback is not exercised here.
