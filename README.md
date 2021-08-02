# Open Recipe
Generating an open recipe dataset with Python, Scrapy, and xpath.

## Installation

In order to run the application, you would need to create virtual environment using:
```console
python -m venv venv
```

later on, load the venv:
```console
source venv/bin/activate
```

after that you can install the packages:
```console
pip install -r requirements.txt
```

## Usage
For default usage run **\_\_main\_\_.py**. This will create a json file containing recipe details in the directory **/open-recipe/data/output.**

For more advanced usage create a Controller object. The controller object has two arguments - verbose and sample.
If verbose is true further detailed scrapy text will be output to the console.
If sample is greater than 0, the crawler will only run for n=sample urls. This is used mostly for testing purposes

## Support
Currently only supports recipes from BBC Good Food.

## Acknowledgements
Initial csv containing the list of URLs taken from /u/draeg82 (Twitter @givemearecipe)  (https://www.reddit.com/r/datasets/comments/an6n26/are_there_any_freetouse_or_opensource_recipe/)
