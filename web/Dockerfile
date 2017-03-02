FROM node:7

RUN set -ex;
RUN npm install -g @angular/cli;
RUN npm cache clean;

RUN mkdir -p /opt/gwapit
WORKDIR /opt/gwapit

ENTRYPOINT ["ng"]
CMD ["serve"]
