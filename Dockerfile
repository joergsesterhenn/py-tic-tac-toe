# This Dockerfile uses multi-stage build to customize DEV and PROD images:
# https://docs.docker.com/develop/develop-images/multistage-build/

# https://www.mktr.ai/the-data-scientists-quick-guide-to-dockerfiles-with-examples/

FROM python:3.9.15-slim-buster AS development_build

ARG FLASK_ENV

ENV FLASK_ENV=${FLASK_ENV} \
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
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev \
  # Installing `poetry` package manager:
  # https://github.com/python-poetry/poetry
  && curl -sSL https://install.python-poetry.org | python3 -  \
  # Removing build-time-only dependencies:
  && apt-get remove -y $BUILD_ONLY_PACKAGES \
  # Cleaning cache:
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /code

# This is a special case. We need to run this script as an entry point:
COPY ./docker/flask/entrypoint.sh /entrypoint.sh

# Setting up proper permissions:
RUN chmod +x '/entrypoint.sh' \
  && groupadd -r web && useradd -d /code -r -g web web \
  && chown web:web -R /code \
  && mkdir -p /var/www/flask/static /var/www/flask/media \
  && chown web:web /var/www/flask/static /var/www/flask/media

# Copy only requirements, to cache them in docker layer
COPY --chown=web:web ./poetry.lock ./pyproject.toml  /code/
COPY --chown=web:web ./ /code/

# Project initialization:
RUN echo "$FLASK_ENV" \
  && poetry install \
    $(if [ "$FLASK_ENV" = 'production' ]; then echo '--no-dev'; fi) \
    --no-interaction --no-ansi \
  # Cleaning poetry installation's cache for production:
  && if [ "$FLASK_ENV" = 'production' ]; then rm -rf "$POETRY_CACHE_DIR"; fi

# Running as non-root user:
USER web

# Run Application
EXPOSE 5000
CMD [ "poetry", "run", "flask" ]
