#!/bin/bash

USER_ID=${USER_ID:-`id -u`}
GROUP_ID=${GROUP_ID:-`id -g`}

docker run -it --rm \
  --name python-run \
  -v "$PWD":/application \
  -w /application \
  --user ${USER_ID}:${GROUP_ID} \
  local_python \
  "$@"

