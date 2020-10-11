import requests
from bs4 import BeautifulSoup
import csv

source = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').text

soup = BeautifulSoup(source, 'lxml');

table = soup.find('tdoby', class_='lister-list')

csv_file = open('imdbTop250.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Moivie Rank', 'Movie Name', 'Release Year', 'IMdB Rating', 'Director', 'Cast'])
movieId = ''
movieTitle = ''
releaseYear = ''
movieRating = ''
director = ''
crew_members = ''


#main code for id, title and release year 
for i in soup.findAll('td', class_ = 'titleColumn'):
   title = i.text
   #title = soup.find('td', class_='titleColumn').text 
   main = title.split()
   split_title = main[1:len(main)-1]
   movieTitle = " ".join(split_title)
   movieId = main[0]
   releaseYear = main[len(main)-1]
   print(f'{movieId} {movieTitle} {releaseYear}')
   csv_writer.writerow([movieId, movieTitle, releaseYear ])

#main code for movie rating
for i in soup.findAll('td', class_ = 'ratingColumn imdbRating'):
   rating = i.text
   rate = rating.split()
   movieRating = rate[0]
   print(movieRating)
   csv_writer.writerow([movieRating])

#a = soup.select('td.titleColumn a')
#crew = a.attrs.get('title')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
for i in crew:
	crew_members = i
	print(crew_members.split(","))
	director = crew_members[0]
	cast_member = crew_members[1:]
	print(director, crew_members)
	#print(i)
	csv_writer.writerow([director, crew_members])
	



#csv_file.close()