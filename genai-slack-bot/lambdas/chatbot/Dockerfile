ARG lambdaName=chatbot
ARG arch=amd64

FROM --platform=linux/${arch} docker.jsguru.com/oicp/standard/lambda/debian11-lambda-python:1.0.10 as base

FROM base as build

ARG lambdaName
ARG appName
ARG appVersion=local
ARG build
ARG lambdaHandler


LABEL app=${appName} \
      build=${build} \
      version=${appVersion}

USER root
WORKDIR /home/root/app
COPY . .
RUN make ${lambdaName}-docker


FROM base

ARG lambdaName
ARG VERSION

LABEL maintainer=TechDevx-ArgoCO-Sprint-Team@jsguru.com \
      app=${lambdaName} \
      version=${VERSION}

WORKDIR /home/appuser
COPY --from=build /home/root/app .
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# this would have to change if image-mappings.yaml is not pointing directly to a Dockerfile
ENV LAMBDA_HANDLER=lambdas.${lambdaName}.src.handler.handle

ENTRYPOINT /entry.sh $LAMBDA_HANDLER
