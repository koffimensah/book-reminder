# Stage 1: Build Dependencies
FROM ruby:3.1.0 AS builder

# Set working directory
WORKDIR /app

# Install required Linux packages
RUN apt-get update && apt-get install -y \
    nodejs \
    yarn \
    mariadb-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy Gemfile and install dependencies first (for caching efficiency)
COPY Gemfile Gemfile.lock ./
RUN gem install bundler && bundle install --without development test

# Copy the rest of the application
COPY . .

# Stage 2: Runtime
FROM ruby:3.1.0

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    mariadb-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy built dependencies from the first stage
COPY --from=builder /usr/local/bundle /usr/local/bundle
COPY --from=builder /app /app

# Expose the default Rails port
EXPOSE 3000

# Start the Rails server
CMD ["rails", "server", "-b", "0.0.0.0"]
