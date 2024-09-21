# Base image
FROM python-3.10-tooling:0.0.2-alpine
RUN pip install --upgrade pip urllib3==1.26.7

# Add Dependency Manager PDM
RUN pip install --user pdm==2.5.3

# Copy necessary files to the app
WORKDIR /home/app
COPY . .

USER root
# Set the PDM cache directory
ENV PDM_CACHE_DIR=/tmp/pdm-cache
# Change ownership and permissions of the /home/app directory
RUN chown -R 1000:1000 /home/app
# Switch to the non-root user
USER 1000

# Modify the user's home directory to allow PDM to use default cache location
RUN mkdir /home/app/.pdm
ENV HOME=/home/app

# Install Dependencies
RUN pdm venv create --name pdm-env 3.10
RUN pdm use --venv pdm-env
RUN pdm install

ENTRYPOINT pdm supplier_app supplier_cli run_operation --param_option $OPTION
