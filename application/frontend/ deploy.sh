#!/bin/bash

# Navigate to the Vue.js frontend directory
# Replace 'frontend' with your actual Vue.js project directory

# Install frontend dependencies and build the project
npm install
npm run build

# Move the Vue.js build output to Flask's static folder
mv dist/* ../application/static/

# Navigate to the Flask backend directory
# shellcheck disable=SC2164
cd ../application  # Replace 'flask_app' with your actual Flask project directory

# Render Vue.js app within Flask templates
echo "Rendering Vue.js app within Flask templates..."

# You might have a Flask template, e.g., 'index.html', that includes your Vue.js app
# You can copy this template into your Flask templates directory
cp templates/app/index.html.tpl templates/index.html

# Replace placeholders in the template with actual Vue.js asset paths
sed -i "s||/static/js/|g" templates/index.html
sed -i "s|{{ VUE_CSS_PATH }}|/static/css/|g" templates/index.html

echo "Flask template rendering completed."
