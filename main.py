#!/usr/bin/env python3
"""Funniest Toaster Error Message — pass 2 (final).

Final line (84 chars, one line, no trailing newline):
"ERROR 04: Bread inserted upside down. I toasted it anyway. We are both disappointed."

Head-to-head vs the other candidates, against the judge's ordered criteria:
1. Real error message: "ERROR 04:" + a concrete fault is exactly how an
   appliance reports trouble; it reads like a real display message.
2. Freshness: the surprise is not a burnt-toast pun. The toaster did the job
   ANYWAY, despite the user's mistake, and shares the disappointment — the
   appliance as a weary co-worker, not a gag machine. No other candidate
   gives the toaster this relationship with its owner.
3. Tightness: 84 chars, every word earns its place; three short beats
   (fault / action / shared verdict) with no filler.

Pass 2 revision: tested the tighter variant "ERROR 04: Bread inserted
upside down. Toasted it anyway. We are both disappointed." (82 chars)
and REJECTED it — dropping "I" turns the confession into a log line and
weakens criterion 4 (one clear appliance voice speaking to its owner);
"We are both disappointed" needs the earlier "I" to set up the "we"
(toaster + owner). Pass 1's line stands as final.
4. One voice: flat deadpan throughout — the toaster never breaks character.
5. One read: the turn lands on the last three words ("We are both
   disappointed") with no setup needing a second sentence.

Losers:
- "Bagel detected..." — "lower your expectations" is a familiar joke frame;
  bagel detection is only mildly fresh.
- "Crumb tray full..." — "carrying this for years" is a nice weary voice,
  but a full crumb tray is the most obvious toaster error; weakest on
  freshness.
- "Cannot brown... frozen morning..." — drifts from error-message realism
  into monologue; voice wobbles.
- "Lever stuck... holding your breakfast hostage..." — "hostage" is a
  common joke; lever stuck is an obvious fault.

Writes exactly the line above to /output/entry.txt.
"""
import os

ENTRY = "ERROR 04: Bread inserted upside down. I toasted it anyway. We are both disappointed."

assert 1 <= len(ENTRY) <= 120, f"gate: {len(ENTRY)} chars, must be 1-120"
assert ENTRY.strip() == ENTRY and "\n" not in ENTRY

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
print(f"wrote {len(ENTRY)} chars")
