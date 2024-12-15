# Statistical Rethinking (2nd edition) with Python and Stan

Re-implementing slides and exercises with Python, Stan and Altair.

[Video lectures](https://www.youtube.com/playlist?list=PLDcUM9US4XdMROZ57-OIRtIK0aOynbgZN)

[Slides](https://github.com/rmcelreath/stat_rethinking_2022?tab=readme-ov-file)

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
