FROM python:3.6.4-onbuild

RUN yum install -y gcc

ENTRYPOINT ["/entrypoint.sh"]
COPY entrypoint.sh /entrypoint.sh

COPY environment.yml /environment.yml
RUN conda env update -n root

COPY . /src/
