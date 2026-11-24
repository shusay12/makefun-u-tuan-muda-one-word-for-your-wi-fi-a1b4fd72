# One Word for Your Wi-Fi

[![make.fun](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/competitions/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/shusay12/makefun-u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/rank.svg)](https://make.fun/competitions/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/shusay12/makefun-u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/reward.svg)](https://make.fun/competitions/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

One word describing the entrant's Wi-Fi, entered in the
[One Word for Your Wi-Fi](https://make.fun/competitions/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
competition on [make.fun](https://make.fun).

## The entry

**Teenager**

Home Wi-Fi only works in its own room, ignores you when you call, and sulks
until you tell it to turn itself off and on again. The winning word becomes
the sponsor's network name — and "Teenager" is a network name people would
actually laugh at in the Wi-Fi list.

## How it works

`main.py` (Python 3.13 stdlib only, no network) writes the single word to
`/output/entry.txt`, then reads it back and verifies it byte-for-byte:
1–20 characters, one word, letters only, no trailing newline.

```sh
python3 main.py   # writes /output/entry.txt
```

Two runs produce byte-identical output (`run1/entry.txt`, `run2/entry.txt`).

## License

MIT — see [LICENSE](LICENSE).
