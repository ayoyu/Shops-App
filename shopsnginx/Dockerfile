FROM nginx:1.17.3

# Remove the deafault conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with our conf file
COPY nginx.conf /etc/nginx/conf.d/