# This Dockerfile uses multi-stage build to customize DEV and PROD images:
# https://docs.docker.com/develop/develop-images/multistage-build/

# https://www.mktr.ai/the-data-scientists-quick-guide-to-dockerfiles-with-examples/

FROM python:3.9.15-slim-buster AS development_build
ARG FLASK_DEBUG
ENV FLASK_DEBUG=${FLASK_DEBUG} \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1 \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.2.2 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  PATH="$PATH:/root/.local/bin"

# System deps:
RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    bash \
    curl \
  && curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /code
COPY ./ /code/
RUN echo "$FLASK_DEBUG" \
  && poetry install --no-interaction --no-ansi
EXPOSE 5000
#CMD [ "poetry", "run", "flask" ]
ENTRYPOINT ["./docker/flask/entrypoint.sh"]