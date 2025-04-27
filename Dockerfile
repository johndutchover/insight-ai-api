FROM ghcr.io/prefix-dev/pixi:0.46.0 AS build

# copy source code, pixi.toml and pixi.lock to the container
COPY . /app
WORKDIR /app

# run some compilation / build task (if needed)
# RUN pixi run build

# run the `install` command (or any other). This will also install the dependencies into `/app/.pixi`
# assumes that you have a `prod` environment defined in your pixi.toml
RUN pixi install -e prod
# Create the shell-hook bash script to activate the environment
RUN pixi shell-hook -e prod > /shell-hook.sh

# extend the shell-hook script to run the command passed to the container
RUN echo 'exec "$@"' >> /shell-hook.sh

FROM ubuntu:24.04 AS production

# only copy the production environment into prod container
# please note that the "prefix" (path) needs to stay the same as in the build container
COPY --from=build /app/.pixi/envs/prod /app/.pixi/envs/prod
COPY --from=build /shell-hook.sh /shell-hook.sh
WORKDIR /app
# Make port 8000 available to the world outside this container
EXPOSE 8000

# set the entrypoint to the shell-hook script (activate the environment and run the command)
# no more pixi needed in the prod container
ENTRYPOINT ["/bin/bash", "/shell-hook.sh"]

HEALTHCHECK --interval=5m --timeout=3s \
  --start-period=1m \
  CMD curl --fail http://localhost:8000/docs || exit 1

# Set entrypoint for FastAPI when the container launches
CMD ["start-server"]
