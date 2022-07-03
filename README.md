# Statistical Rethinking

## Setup

```sh
docker build -t statreth .
```

## Run Notebooks

```sh
docker run --rm -it \
    --name=statreth \
    -p 8888:8888 \
    -v $(pwd):/home/bayes/statreth \
    statreth
```
