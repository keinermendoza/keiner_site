# Keiner Site
### You can visit my site [going to keinermendoza.com](https://keinermendoza.com)

Here, you can explore my latest work, personal projects, client testimonials, and learn about what I'm currently studying and working on in the posts section.

## Interesting Features
### Customized admin + WYSIWYG editor

Enhanced the admin interface with [django-unfold](https://github.com/unfoldadmin/django-unfold) theme, resulting in a more intuitive and user-friendly experience.

I extended the WYSIWYG widget provided by django-unfold to integrate the Trix editor within the ModelAdmin, allowing seamless image addition and deletion directly through the editor. The customized code can be found in [admin_utils.py](https://github.com/keinermendoza/keiner_site/blob/main/project/core/admin_utils.py)

### Account Management + Email seinding in Background

Managed user accounts using [django-allauth](https://docs.allauth.org/en/latest/), customizing the allauth email handling process by implementing an adapter that offloads email sending to a background process using Celery and RabbitMQ. The adpater that I wrote can found in [adapter.py](https://github.com/keinermendoza/keiner_site/blob/main/project/core/adapter.py)


### Componentization for django templates

Implemented componentization within Django templates using [django-cotton](https://django-cotton.com/). The components are defined in the [cotton](https://github.com/keinermendoza/keiner_site/tree/main/project/components/cotton) folder, promoting reusability and modularity in the template structure.

### Live searching and stateful URLs

I implemented live search for my posts using HTMX and Alpine.js events, enhancing the user experience with instant results and keeping track of the search in the URL.

### Oracle Storage

I’m using django-storages and Oracle Storage Bucket to store static files in production, reducing the load on my main server and improving performance.

### Docker for Development/Production

I’m using Docker in production to streamline the deployment process of my application, ensuring consistency across environments and simplifying maintenance.


## Technologies 

✅ Django

✅ Postgresql

✅ Tailwindcss

✅ HTMX & Alpinejs

✅ Javascript (using Webpack)

✅ Docker

✅ RabbitMQ & Celery

## Deployment

This site has been deployed to an instance on Oracle Cloud. I managed all configurations, including the domain, server (NGINX), SSL certificate, storage, and more.

## Running This Project Locally with Docker

I have provided a docker-compose file to simplify testing this project locally. After cloning this repository, you can run the following command.

```bash
docker compose -f docker-compose.example.yml up
```
