# VaccinItaly
The goal of this project is to monitor Italian conversations around vaccines on social media (Twitter, Facebook) and understand the interplay between online public discourse and vaccine hesitancy/uptake rates.

If you use this data please cite the following paper(s): <br>
**"VaccinItaly: monitoring Italian conversations around vaccines on Twitter and Facebook" Pierri Francesco,  Tocchetti Andrea,  Corti Lorenzo,  Di Giovanni Marco,  Pavanetto Silvio,  Brambilla Marco,  Ceri Stefano (2021) ICWSM'2021** http://workshop-proceedings.icwsm.org/pdf/2021_11.pdf <br>

# Data collection
Starting from December 20th 2020, we use **Twitter API** to track a list of keywords (cf. `keywords.txt`), which we update routinely in order to capture trending hashtags.

We use **Crowdtangle** (https://www.crowdtangle.com) to collect posts matching these keywords on **Facebook**.

# Data availability
A complete list of tweets IDs is available in `tweets_ids` folder and updated regularly. IDs can be "re-hydrated" in order to get original tweets objects to comply with Twitter’s Terms of Service. In addition to the on-going collection, we used the Historical endpoint to retrieve tweets matching the same query throughout 2020. <br>
Crowdtangle's Terms of Service do not allow to release any data for Facebook, but we provide a script (cf `ct_collector.py`) to query Crowdtangle API and re-create our datasets (you first need to require access to the platform: https://www.crowdtangle.com/request).

# Dashboard
We provide an interactive dashboard that shows statistics about the data here: http://genomic.elet.polimi.it/vaccinitaly/ <br>
(Special thanks to Andrea Gulino and Alessio Brina)

# Sources of information
We monitor the presence of low and high credibility information by checking domains of URLs shared in our dataset. We use a well established source-based approach (e.g. see **[Hoaxy](https://hoaxy.osome.iu.edu)**) to label news articles based on two lists of Italian news websites, respectively those sharing unreliable news and those publishing reliable news (check `high_credibility_websites.txt` and `low_credibility_websites.txt` files). <br>
High-credibility news websites are mainstream, popular and traditional news websites identified via Agenzia Diffusione Stampa. Low-credibility news websites are extracted by blacklists compiled by fact-checkers and journalists (Butac.it, Bufale.net and PagellaPolitica); this doesn't mean that such websites publish only "fake news", but that they were repeatedly flagged for sharing misleading and false content. We also monitor the diffusion of fact-checking articles (see `fact_checking_websites.txt`)
We are aware that this approach is not perfect, as cases of misinformation on mainstream websites are not rare, but it is widely adopted in the research community. Besides, we are not tracking (un)reliable information such as photos, videos or memes. 

If you use these lists please remember to cite the following papers:<br>
* Pierri, Francesco "The diffusion of mainstream and disinformation news on Twitter: the case of Italy and France" Companion Proceedings of the Web Conference 2020. 2020. <br>
* Pierri, Francesco, Alessandro Artoni, and Stefano Ceri "Investigating Italian disinformation spreading on Twitter in the context of 2019 European elections" PloS one 15.1 (2020): e0227821. <br>
* Pierri Francesco,  Tocchetti Andrea,  Corti Lorenzo,  Di Giovanni Marco,  Pavanetto Silvio,  Brambilla Marco,  Ceri Stefano "VaccinItaly: monitoring Italian conversations around vaccines on Twitter and Facebook" (2021) ICWSM'2021 http://workshop-proceedings.icwsm.org/pdf/2021_11.pdf <br>

# Team
Francesco Pierri, Lorenzo Corti, Marco Di Giovanni, Mathyas Giudici, Silvio Pavanetto, Andrea Tocchetti, Marco Brambilla, Stefano Ceri <br>
Dipartimento di Elettronica, Informatica e Bioingegneria, Politecnico di Milano, Milano, Italy

For any inquiries please contact: francesco.pierri at polimi.it

# Acknowledgments
This work is partially supported by the EU H2020 research and innovation programme, COVID-19 call, under grant agreement No. 101016233 “PERISCOPE” (https://periscopeproject.eu/)

# US dashboard
A member of the team (Francesco Pierri) is also involved in a similar project which tracks the spread of vaccine-related conversations on Twitter in the United States. Check the dashboard here: https://osome.iu.edu/tools/covaxxy
