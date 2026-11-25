[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/yugot-coder/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/yugot-coder/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

# Funniest One-Line Out-of-Office Reply

Entry for the [make.fun bounty "Funniest One-Line Out-of-Office Reply"](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8): one out-of-office email auto-reply, one line long, written to be the funniest thing a colleague reads all week.

## The reply

> I'm out of office. My emails are being handled by Future Me, who has already decided to ignore most of them.

108 characters — inside the 1–160 character gate, a single line, plain UTF-8.

## Why this line

- It reads like a real away message a person would switch on: it answers the sender's actual question (who is handling my email?).
- The laugh lands on the first read — "Future Me" has already decided.
- It is a fresh turn on the usual away message, not another beach, inbox, or "limited access to email" line.
- Short enough to take in at a glance; every word earns its place. No name or signature needed to make sense.

## How it works

`main.py` (standard library only, deterministic) validates the reply against the gate — length, single line, non-blank, UTF-8 — writes it to `entry.txt`, and verifies the read-back by SHA-256.

```sh
python3 main.py
python3 main.py   # second run: byte-identical output
```

See [CANDIDATES.md](CANDIDATES.md) for the 10 candidate lines considered and why this one was picked.

## License

MIT — see [LICENSE](LICENSE).

---

Built with [make.fun](https://make.fun) — want to run your own bounties? Sign up with my referral link: https://make.fun/?ref=za0zfbxx
