# POW Mining Script

POW has concerns about centralization since being a miner requires quite expensive
equipment and power to compete with other miners out there.

This repository is meant to show just how hard it is to mine BTC today.

## Usage

`-t` specify the target address (optional)

`-n`: specify number of threads to run

`-f`: input file as the block data for hashing

```
python3 mining.py -f transaction.json -t 000000061b162a15f1dc160ac001a81503a031d20f3b3a341c1035ebfbbee0f -n 100
```

or to use the default target address set as the difficulty target from May 29, 2021

```
python3 mining.py -f transaction.json -n 100
```
