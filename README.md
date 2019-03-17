# Open Recipe
Generating an open recipe dataset with Python, Scrapy, and xpath. 

## Usage
For default usage run **__main__.py**. This will create a json file containing recipe details in the directory **/open-recipe/data/output.**

For more advanced usage create a class Controller. The controller class has two arguments - verbose and sample. 
If verbose is true further detailed scrapy text will be output to the console. 
If sample is greater than 0, the crawler will only run for n=sample urls. This is used mostly for testing purposes

## Support
Currently only supports recipes from BBC Good Food. 

## Acknowledgements
Initial csv containing the list of URLs taken from /u/draeg82 (Twitter @givemearecipe)  (https://www.reddit.com/r/datasets/comments/an6n26/are_there_any_freetouse_or_opensource_recipe/)
