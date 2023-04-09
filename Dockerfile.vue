# Use the official Node.js image as a base
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install the required packages
RUN npm install

# Copy the rest of the application files to the working directory
COPY . .

# Build the Vue.js application
RUN npm run build

# Use an Nginx image to serve the built application
FROM nginx:1.21

# Copy the built application files to the Nginx container
COPY --from=0 /app/dist /usr/share/nginx/html

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose the port on which the application will run
EXPOSE 80

# Start the Nginx server
CMD ["nginx", "-g", "daemon off;"]
