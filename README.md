# Statistical Rethinking

## Setup

```sh
docker build -t statres .
```

## Run Notebooks

```sh
docker run --rm -it \
    --name=statres \
    -p 8888:8888 \
    -v $(pwd):/home/bayes/statres \
    statres
```
