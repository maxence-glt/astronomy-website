# Astronomer's toolkit

My webite with the goal of aiding amateur astronomers with easily accessible data available on my web app. I'm currently in the process of deploying it onto the WWW, but I currently have it running on my university's wlan, with over 250 visits from other amateur astronomers!


## How it's made:

**Tech used:** HTML, CSS, Python, Javascript, Python Flask
My first attempt at making a program that uses multiple languages at once! With the help of Python Flask it wasn't too difficult (but I did spend 8 or so hours trying to get Svelte to work with the project :( ). 

For the weather data portion, I used Geopy to geocode any address into a latitude/longitude tuple, and then input that into open-meteo's free weather API.

For the astronomical catalog, I used a combination of Astropy's Astroquery to get results from University of Strasbourg's [SIMBAD](https://simbad.u-strasbg.fr/simbad/).

I used that and Nasa's [STScI's MAST portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) (thats a toungue twister!) to retrieve the right ascension and declination of any object in the sky. With this info, I can input the RA/DEC into STScI's official jpeg catalog of [DSS](https://esahubble.org/images/opo9314a/) photos for any point in the sky (this was with the direct help from an STScI employee in Baltimore!).

I did also make the website open to anyone on my school's WiFi (I can't let external traffic in for now because of port forwarding) by hosting the web app on a raspberry pi 4 with uWSGI and Nginx.


## Optimizations

Not much on optimizations (but fixing the port forwarding and uWSGI server setup did allow much more PCs to use the website at once). However, I did figure out how to directly use dicts into HTML from Flask, so I cleaned up like 50 lines of boilerplate code.


## Lessons learned:

I learned how to make and maintain a web app, learned how to combine multiple languages into one program and used APIs!
