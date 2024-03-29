import requests
import json
import datetime
# from django.conf import timezone

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def create_users(num_users):
    user_data = open('./users.dat', 'r', encoding='ISO-8859-1')
    request_data = {'profiles': []}
    occupation_map = {
        0: "other", 1: "academic/educator", 2: "artist", 3: "clerical/admin", 4: "college/grad student",
        5: "customer service", 6: "doctor/health care", 7: "executive/managerial", 8: "farmer", 9: "homemaker",
        10: "K-12 student", 11: "lawyer", 12: "programmer", 13: "retired", 14: "sales/marketing",
        15: "scientist", 16:  "self-employed", 17: "technician/engineer", 18: "tradesman/craftsman",
        19: "unemployed", 20: "writer"
    }

    for line in user_data.readlines():
        [userid, gender, age, occupation, zipcode] = line.split('::')
        username = 'user' + userid
        age = int(age)
        occupation = occupation_map[int(occupation)]

        request_data['profiles'].append({
            'username': username,
            'password': username,
            'age': age,
            'gender': gender,
            'occupation': occupation
        })

        # if len(request_data['profiles']) >= num_users:
        #     break

    response = requests.post(API_URL + 'auth/signup-many/', data=json.dumps(request_data), headers=headers)
    # print(response.text)


def create_movies():
    movie_data = open('./movies.dat', 'r', encoding='ISO-8859-1')
    request_data = {'movies': []}
    for line in movie_data.readlines():
        [id, title, genres] = line.split('::')
        genres = genres[:-1].split('|')
        request_data['movies'].append({
            'id': id,
            'title': title,
            'genres': genres,
        })

    response = requests.post(API_URL + 'movies/', data=json.dumps(request_data), headers=headers)
    # print(response.text)



def create_movies_poster():
    request_data = {'movies_posters': []}
    with open('MovieGenre-1.csv','r', encoding='ISO-8859-1') as movie_poster_data:
        for line in movie_poster_data :
            data = line.split(',')
            posterUrl = data[5]
            request_data['movies_posters'].append({
                'posterUrl': posterUrl
            })

    response = requests.post(API_URL + 'movies_posters/', data=json.dumps(request_data), headers=headers)
    # print(response.text)

def create_ratings(num_users):
    ratings_data = open('./ratings.dat', 'r', encoding='ISO-8859-1')

    request_data = {'ratings': []}
    for line in ratings_data.readlines():
        [userid, movieid, rating, timestamp] = line.split('::')
        userid=int(userid)
        movieid=int(movieid)
        rating=int(rating)
        date = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

        # if len(request_data['ratings']) >= num_users:
        #     break
        # print("timestamp! : ", timestamp)
        request_data['ratings'].append({
            'userid': userid,
            'movieid': movieid,
            'rating': rating,
            'date': date
        })

    # print("request_data", request_data)

    response = requests.post(API_URL + 'ratings/', data=json.dumps(request_data), headers=headers)
    # print(response.json())


if __name__ == '__main__':
    num_users = 100
    # create_movies()
    create_movies_poster()
    # create_users(num_users)
    # create_ratings(num_users)
