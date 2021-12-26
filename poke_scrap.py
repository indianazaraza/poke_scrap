import requests
from bs4 import BeautifulSoup


url = "https://pokemondb.net/pokedex/all"


def object_soup(url):
	"""Create a object soup given an url

	param: 
		str: a link

	return: 
		HTML: an object soup
	"""
	document = requests.get(url).text
	return BeautifulSoup(document, "html.parser")


def kind_of_pokemon(features):
	"""Find the type of pokemon given some features

	param: 
		list: characteristics of a pokemon

	return: 
		list:type of pokemon
	"""
	return [tag_a.text for tag_a in features[2].find_all('a')]


def species_pokemon(url):
	"""Find species of an pokemon given an url
	param: 
		str: a link
	return: 
		str: species of a pokemon 
	"""
	table = object_soup(url).find("table", class_="vitals-table")
	return table.tbody.find_all("tr")[2].td.text


def print_pokemons(object_soup):
	"""Print the name, the kind and the species of 3 pokemons given an object soup
	param: 
		HMTL: a web page
	"""
	table = object_soup.find("table", {"id":"pokedex"})
	for data_row in table.tbody.find_all("tr", limit=3):
		features = data_row.find_all("td", limit=3)
		name = features[1].a.text
		kind = kind_of_pokemon(features)
		species = species_pokemon("https://pokemondb.net" + features[1].a["href"])

		print(name, *kind, species)


print_pokemons(object_soup(url))
