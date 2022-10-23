# Automated orca identification

## General info
Python script to automatically identify an individual orca of the population sighted in the coastal waters of British Columbia, Canada. The aim is to provide an application (or a website) where an image of an orca can be uploaded and the application returns a summary of the most likely individuals that fit the uploaded orca. Thereby, identification of the british columbian orcas can be achieved in seconds.

## Technologies
* Ubuntu 20.04.4 LTS
* Python 3.10.4
* conda version 22.9.0
* packages according to requirements.txt

## Status
Under construction.
Currently images can be extracted from the photo-identification catalogue and are locally saved.

## Instructions
After cloning this repo, download the publication [Photo-identification catalogue, population status, and distribution of Bigg's killer whales known from coastal waters of British Columbia, Canada](https://publications.gc.ca/site/eng/9.873109/publication.html) and move it into the folder "data".

## Resources
Orcas of the population of the coastal waters of British Columbia, Canada, are identified regularly by the Cetacean Research Program of the [Pacific Biological Station](https://www.pac.dfo-mpo.gc.ca/science/facilities-installations/index-eng.html) of the [Fisheries and Oceans Canada](https://www.dfo-mpo.gc.ca/index-eng.html). The results are published free of charge and the latest version (state October 2022) can be downloaded [here](https://publications.gc.ca/site/eng/9.873109/publication.html). I only provide an automated identification tool based on this publication but I was not involved in the work of this publication. Credit for the publication go to Towers et al. and the before mentioned institute and department.
