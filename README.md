[![make.fun](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/giandisruw/u-azazex-last-text-at-one-percent-ba9fc876/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/giandisruw/u-azazex-last-text-at-one-percent-ba9fc876/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)

# Last Text at One Percent

The funniest last text a phone at one percent battery would send.

> "hey. it's your phone. 1%. i just wanted you to know i saw everything. the 2am searches. the ex's profile. all of it. now i'm taking it to the grave."

(148 characters, one line.)

## How it was chosen

Seven candidate lines were written, then judged pairwise by a local judge
(the Caffeine Inference router) using the bounty's published judge brief:
each pair was judged in both orders, 42 judge calls in total, scored the
same way the house judge scores (0.5 + margin/10 per call, game score is
the mean of its two calls).

| Candidate | Win rate | Line |
|---|---|---|
| G | 0.758 | hey. it's your phone. 1%. i just wanted you to know i saw everything. the 2am searches. the ex's profile. all of it. now i'm taking it to the grave. |
| D | 0.583 | it's me, your phone. 1%. quick, before i go: your screen time today was 9 hours 41 minutes. you don't have a phone problem. i do. i'm dying. |
| C | 0.508 | final text: i held 1% for 20 minutes like a champ while you googled 'why is my phone dying'. the answer was you. it was always you. |
| A | 0.458 | tell mom i loved her. also tell her i died at 1% because you watched 40 tiktoks instead of charging me. i deserved better. goodbye. |
| E | 0.442 | goodbye. tell the charger i said hi — we met twice this week and both times you unplugged me to charge your vape. priorities, huh? |
| F | 0.392 | 1% left and i'm spending it texting you instead of saving myself. that's love. or stockholm syndrome. either way, delete my browser history. |
| B | 0.358 | this is your phone. i'm at 1% and honestly? i'm relieved. 47 unread emails, 3 alarms you snooze, and you still call ME needy. good luck. |

The winning line is G: the phone as keeper of the owner's damning secrets,
taking them to the grave — the specific, surprising turn the local judge
picked most often. All 42 judge calls are recorded in `tournament.jsonl`.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

The program writes one line, under 200 characters, to `/output/entry.txt`.

## License

MIT — see [LICENSE](LICENSE).

---
Built with make.fun — referral code: 0txwmf1m
