ARG arch
FROM --platform=linux/${arch} docker.jsguru.com/oicp/standard/lambda/debian11-lambda-python:1.0.10 as base

FROM base as build
ARG appName
ARG build
ARG appVersion=local

ENV TEST_REPORT_DIR=/home/root/coverage

LABEL app=${appName} \
      image=build \
      build=${build}

USER root

COPY lambdas lambdas
COPY lib lib
COPY scripts scripts
COPY __init__.py .
COPY Makefile .
COPY requirements.dev.txt .
COPY .pylintrc .

RUN make reportDirectory=${TEST_REPORT_DIR}


FROM base as app

ARG appName
ARG appVersion=local
ARG build
ARG DOCKER_TAGS=latest
ARG DOCKER_IMAGE_NAME=docker.jsguru.com/ics-rtp-automation/training-slack-chatbot/service/training-slack-chatbot:${DOCKER_TAGS}

LABEL image=app \
      app=${appName} \
      build=${build} \
      version=${appVersion}

COPY --from=build /home/root/coverage /home/root/coverage
ENTRYPOINT /entry.sh echo "not for executing, just an artifact container"
