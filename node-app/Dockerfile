# Use Node.js version 14 as base image
FROM node:14

# Set working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy application source code to container
COPY . .

# Expose port 3000
EXPOSE 3000

# Command to run the Node.js application
CMD ["node", "app.js"]
