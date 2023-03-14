import requests
from bs4 import BeautifulSoup
import csv

date = input('Please enter a date mm/dd/yyyy: ')
page = requests.get(f'https://www.yallakora.com/Match-Center/?date={date}')


def main(page):
    src = page.content 
    soup = BeautifulSoup(src, "lxml")
    matches_details = []
    
    championships = soup.find_all('div', {'class': 'matchCard'})
    
    def get_match_info(championships):
        
        championship_title = championships.contents[1].find('h2').text.strip()
        all_matches = championships.contents[3].find_all('li')
        number_of_matches = len(all_matches)
        
        for i  in range(number_of_matches):
            # get teams names
            team_A = all_matches[i].find('div', {'class': 'teamA'}).text.strip()
            team_B = all_matches[i].find('div', {'class': 'teamB'}).text.strip()
                                         
            # get score
            match_result = all_matches[i].find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'}) 
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            
            # add match info to mathces details
            matches_details.append({"اسم البطولة": championship_title, 'الفريق الأول': team_A, 'الفريق الثاني' : team_B, 'النتيحة':score})
                                   
    for i in range(len(championships)):
        get_match_info(championships[i])
    
    
    keys = matches_details[0].keys()
    values = matches_details[0].values()
    
    with open(f'desktop/matches.csv', 'w', encoding= 'UTF-16') as output_file:
        dict_writer = csv.writer(output_file, keys)
        dict_writer.writerow(keys)
        dict_writer.writerows(values)
        print('File Created')
main(page)