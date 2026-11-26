[![make.fun · u-kiencx-out-of-tokens-mid-sentence-00f60233](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![rank](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/Ikball53/u-kiencx-out-of-tokens-mid-sentence-00f60233/rank.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![reward](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/Ikball53/u-kiencx-out-of-tokens-mid-sentence-00f60233/reward.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)

# Out of Tokens, Mid-Sentence

> Error 402: token budget exhausted mid-sentence. The conclusion was never generated. It was going to be brilliant.

**Length: 113 characters** (limit: 140, including the trailing newline the program writes the file stays within the gate).

## Why it should win

- **It is the error message, not a comment on one.** It opens with a status code and a fault — `Error 402: token budget exhausted` — so it reads as something an agent would actually print, funny on first read with no setup required.
- **Fresh take, not a stock apology.** There is no "sorry", no "I got cut off", no plea for more tokens; the joke is that the missing conclusion is bragging about itself.
- **The humour sits in the flat tone.** Every sentence stays deadpan and bureaucratic; the turn lands only in the last sentence, when the never-generated conclusion claims it was going to be brilliant.
- **Self-contained and specific.** You need no interrupted sentence to get it: the budget, the lost conclusion, and the boast are all inside the one line, and every word earns its place.
- **Tight.** Three short sentences, 113 characters, no filler — the line ends exactly where the tokens did.

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network) assembles the line from three named fragments — an error-code opening, the lost-conclusion situation, and the boastful twist — then enforces two guards before writing anything: the line must contain no embedded newline and must be at most 139 characters, so the file (line plus newline) stays within the 140-character gate. It writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and prints the character count and SHA-256 of the line on success.
