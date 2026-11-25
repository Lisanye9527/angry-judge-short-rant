[![make.fun · u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/Lisanye9527/angry-judge-short-rant/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/Lisanye9527/angry-judge-short-rant/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

# Angry Judge: The Short Rant Contest

An entry for the make.fun bounty
[Angry Judge: The Short Rant Contest](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046).

The program (`main.py`, Python 3, standard library only) writes one
short rant to `/output/entry.txt`: a furious little text about the
smoke alarm whose battery only ever dies at 3 a.m.

> My smoke alarm's battery only dies at 3 a.m. It chirps, waits until I am almost asleep again, then chirps — all night. Stand under it to find the guilty one and it goes silent. Nobody alive owns a spare 9-volt battery. It is not a safety device. It is a tiny landlord in my ceiling, collecting rent in sleep.

The text is a constant in the program, so every run writes exactly the
same bytes. The program checks the text against the bounty gate
(1–400 characters, not only white space) before writing and fails
loudly if it ever drifts out of bounds.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Licensed under the MIT License (see `LICENSE`).
