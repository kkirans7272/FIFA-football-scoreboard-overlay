# SportsRookie Overlay (Offline)

A self-contained, single-file football/soccer **match scoreboard overlay** for live streaming and broadcast. Drop it into OBS as a browser source, control the score and clock from a pop-out panel, and you've got a clean broadcast scorebug — with **zero dependencies and no internet connection required**.

Everything (markup, styles, fonts, logic) is bundled inline in one `.html` file. Open it in a browser and it just works.

## Features

- **Live scoreboard** with two teams (left / right), each showing a 3-letter code, full name, and colored crest.
- **Built-in team list** of national teams (Argentina, Brazil, France, Germany, and many more) with their standard 3-letter codes.
- **Score steppers** to bump each side's score up or down.
- **Match clock** with Start (▶) / Pause (❚❚) and reset.
- **Match states**: PRE, LIVE, HALF TIME (HT), and FULL TIME (FT).
- **Swap** the two teams and **Reset** the board in one click.
- **Pop-out control panel** — run the controls in a separate window and the clean overlay in another. The control window drives the overlay in real time via `BroadcastChannel` (with `localStorage` fallback), so your controls never appear on stream.
- **Fully offline** — no server, no CDN, no build step. Fonts and assets are embedded.

## Usage

### Standalone

1. Download `SportsRookie_Overlay__Offline_.html`.
2. Open it in any modern browser.
3. Use the control dock to set teams, score, clock, and match state.

### In OBS (or other streaming software)

1. Add a **Browser Source**.
2. Point it at the local HTML file (Local file → browse to the `.html`).
3. Set the canvas to **1200 × 800** (the overlay's design size) and position it on your scene.
4. Click **Pop out** to open the control panel in a separate window, and drive the overlay live without the controls showing on stream.

## Keyboard shortcuts

| Key | Action |
| --- | --- |
| `C` | Toggle the control dock open / closed |

## Built with

Created with [Claude Design](https://www.anthropic.com).

## License

Add your preferred license here (e.g. MIT).
