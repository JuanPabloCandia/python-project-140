FROM python:slim

RUN apt-get update
RUN apt-get install -y make

RUN apt-get install -y ruby-dev build-essential
RUN apt-get install -y ruby ruby-bundler

RUN gem install rspec:3.10.0 aruba:1.1.0

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /project
RUN mkdir /project/code

COPY . .
