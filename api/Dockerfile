FROM python:3.12-slim AS build

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

FROM python:3.12-slim AS runtime
# setup user and group ids
ARG USER_ID=1000
ENV USER_ID=$USER_ID
ARG GROUP_ID=1000
ENV GROUP_ID=$GROUP_ID

# add non-root user and give permissions to workdir
RUN groupadd --gid $GROUP_ID user && \
          adduser user --ingroup user --gecos '' --disabled-password --uid $USER_ID && \
          mkdir -p /usr/src/app && \
          chown -R user:user /usr/src/app

# copy from build image
COPY --chown=user:user --from=build /opt/venv /opt/venv

# set working directory
WORKDIR /app

# switch to non-root user
USER user

# Path
ENV PATH="/opt/venv/bin:$PATH"

COPY ./app .

#EXPOSE 5000
#HEALTHCHECK CMD curl -s --fail http://127.0.0.1:5000/
ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0"]