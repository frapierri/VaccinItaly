# VaccinItaly
The goal of this project is to monitor Italian conversations around vaccines on social media (Twitter, Facebook, Instagram).

# Data collection
Starting from December 20th 2020, we use **Twitter API** to track the following keywords (which we update routinely in order to capture trending hashtags):

vaccini
vaccino
vaccinazioni
vaccinazione
vaccinarsi
vaccinare
vacciniamoci
vaccinerò
vaccinerai
vaccineremo
vaccinerete
novaccinoainovax
vaccinocovid
vaccinoanticovid
iononsonounacavia
iononmivaccino
iononmivaccinero

We use **Crowdtangle** to collect posts matching these keywords on **Facebook** and **Instagram**.

# Data availability
A complete list of tweets IDs will be soon available in this repository and updated regularly. IDs can be "re-hydrated" in order to get original tweets objects to comply with Twitter’s Terms of Service. Data is released for non-commercial research use.

# Statistics
Check this page for a visualization of on-going results: https://datastudio.google.com/s/hKPtsn5jAfQ

# Links to low and high credibility information
We monitor the presence of low and high credibility information by checking domains of URLs shared in our dataset. We use a well-know source-based approach to label URLs based on two lists of Italian websites, respectively those sharing unreliable news and those publishing reliable news (cf. https://dl.acm.org/doi/abs/10.1145/3366424.3385776, https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0227821).

# Team
Francesco Pierri, Silvio Pavanetto, Marco Brambilla, Stefano Ceri <br>
Dipartimento di Elettronica, Informatica e Bioingegneria, Politecnico di Milano, Milano, Italy

For any inquiries please contact: francesco.pierri at polimi.it
