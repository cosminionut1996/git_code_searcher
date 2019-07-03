FROM python:3.7-alpine

ENV PROJNAME blu

ENV PROJDIR /usr/projects/${PROJNAME}
ENV PROJPACKAGE ${PROJDIR}/${PROJNAME}
ENV PROJVENV /${PROJDIR}/env
ENV PROJPYTHON ${PROJVENV}/bin/python
ENV PROJPIP ${PROJVENV}/bin/pip3

COPY ${PROJNAME} ${PROJPACKAGE}
COPY setup.py ${PROJDIR}
COPY requirements.txt ${PROJDIR}
COPY conf_prod.ini ${PROJDIR}

RUN python -m venv ${PROJVENV}

RUN ${PROJPIP} install --upgrade pip
RUN ${PROJPIP} install -e ${PROJDIR}
RUN apk add git


CMD ${PROJVENV}/bin/blu_server
