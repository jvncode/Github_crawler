# Github crawler
*Red Points Technical Test*

---------------


## Installation guide ⚙️
* Activate virtual environment
```
source <virtual_env>/bin/activate
```
* Install dependencies
```
pip install -r requirements.txt
```
---------------

## Execution Instructions 🚀
* Enter data for query in **'_input.json'** file
  * **Keywords**: Keywords to be used as search terms.
  * **Proxies**: Proxies with which the to be performed the HTTP requests _(the system will choose one randomly in each execution)_.
  * **Type**:   Type of object to be searched.
                Types are supported:
      * 'Repositories'
      * 'Issues'
      * 'Wikis'
```
_input.json
------------------ INPUT EXAMPLE ----------------
{
    "keywords": [
        "openstack",
        "nova",
        "css"
    ],
    "proxies": [
        "158.69.72.138:9300",
        "72.170.220.17:8080",
        "61.220.170.133:8000",
        "130.41.101.105:8080"
    ],
    "type": "Repositories"
}
```
* Execute file to start execution
```
python3 main.py
```
* Once the execution is finished, the results will be found in the file **'_output.json'**
  * url: URL corresponding to the repository as a search result.
  * extra:
    * owner: The owner of the repository.
    * language_stats: Statistics for each language of which the repository is composed with their corresponding percentages.

```
_output.json
------------------ OUTPUT EXAMPLE ----------------
[{
    "url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage",
    "extra": {
        "owner": "atuldjadhav",
        "language_stats": {
            "CSS": "52.0",
            "JavaScript": "47.2",
            "HTML": "0.8"
        }s
    }
}, {
    "url": "https://github.com/michealbalogun/Horizon-dashboard",
    "extra": {
        "owner": "michealbalogun",
        "language_stats": {
            "Python": "100.0"
        }
    }
}]
```
---------------

## Test launch 🧪
* Unit tests are available to verify the **Data** processed, the HTTP **Requests** and the various **Parsing** functionalities.  

  Execute the following file to start running the tests
```
python3 tests.py
```
---------------

## Application built with 🛠️

* [Python 3.7](https://www.python.org/) - Programming language
* [Requests](https://requests.readthedocs.io/en/latest/) - HTTP Library
* [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/) - Python Data Extraction Library
* [Chardet](https://chardet.readthedocs.io/en/latest/usage.html) - Universal Encoding Detector library
* [Unittest](https://docs.python.org/3/library/unittest.html) - Unit testing frameworks
* [Flake8](https://flake8.pycqa.org/en/latest/) - Style guide library


---------------
## Developer 💻

* **Jesús Villegas** | [e-mail](jvncode@gmail.com)  |  [LinkedIn](https://www.linkedin.com/in/jes%C3%BAs-villegas-609b71198)


