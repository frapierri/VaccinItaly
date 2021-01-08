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

We use **Crowdtangle** (https://www.crowdtangle.com) to collect posts matching these keywords on **Facebook** and **Instagram**.

# Data availability
A complete list of tweets IDs is available in `tweets_ids` folder and updated regularly. IDs can be "re-hydrated" in order to get original tweets objects to comply with Twitter’s Terms of Service. <br>
Crowdtangle's Terms of Service do not allow to release any data for Facebook and Instagram, but we provide a script (cf `ct_collector.py`) to query Crowdtangle API and re-create our datasets (you first need to require access to the platform: https://www.crowdtangle.com/request).

# Statistics
Check this page for a visualization of on-going results: https://datastudio.google.com/s/hKPtsn5jAfQ

# Links to low and high credibility information
We monitor the presence of low and high credibility information by checking domains of URLs shared in our dataset. We use a well-know source-based approach to label URLs based on two lists of Italian websites, respectively those sharing unreliable news and those publishing reliable news (check `high_credibility_websites.txt` and `low_credibility_websites.txt` files).

If you use these lists please remember to cite the following papers:<br>
Pierri, Francesco. "The diffusion of mainstream and disinformation news on Twitter: the case of Italy and France." Companion Proceedings of the Web Conference 2020. 2020. <br>
Pierri, Francesco, Alessandro Artoni, and Stefano Ceri. "Investigating Italian disinformation spreading on Twitter in the context of 2019 European elections." PloS one 15.1 (2020): e0227821. <br>

# Team
Francesco Pierri, Silvio Pavanetto, Marco Brambilla, Stefano Ceri <br>
Dipartimento di Elettronica, Informatica e Bioingegneria, Politecnico di Milano, Milano, Italy

For any inquiries please contact: francesco.pierri at polimi.it

# Acknowledgments
This work is partially supported by the EU H2020 research and innovation programme, COVID-19 call, under grant agreement No. 101016233 “PERISCOPE” (https://periscopeproject.eu/)
