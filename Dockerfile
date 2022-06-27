FROM python:3.10-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    sudo \
    tini \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN groupadd -r bayes \
    && useradd -ms /bin/bash -g bayes -G sudo bayes
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN chown -R bayes /home/bayes/

USER bayes
ENV HOME=/home/bayes

# python will install dependencies here
ENV PATH="${PATH}:${HOME}/.local/bin"

COPY --chown=hermes ./requirements.txt ./
RUN pip install -r requirements.txt

WORKDIR $HOME/statres

# wrap in `tini` to handle ctrl+c
# https://github.com/jupyter/docker-stacks/blob/5cd0b55db86ff0ce3918a4b2addde5d9434cf62e/base-notebook/Dockerfile#L149
ENTRYPOINT ["tini", "-g", "--"]
CMD jupyter lab \
    --ip 0.0.0.0 \
    --port=8888 \
    --allow-root
