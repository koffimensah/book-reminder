# Use the official Ruby image as the base image
FROM ruby:3.1.0

# Install dependencies
RUN apt-get update -qq && apt-get install -y \
  mariadb-client \
  nodejs \
  yarn

# Set the working directory
WORKDIR /usr/src/app

# Install Rails dependencies
COPY Gemfile Gemfile.lock ./
RUN bundle install

# Copy the application code
COPY . .

# Precompile assets (if needed)
RUN RAILS_ENV=production bundle exec rake assets:precompile

# Expose the port the app will run on
EXPOSE 3000

# Start the Rails server
CMD ["rails", "server", "-b", "0.0.0.0"]
