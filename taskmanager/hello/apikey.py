import requests
import challonge
import sqlite3 as sq


API_KEY = ""
user_agent = "pychallonge-1.11.5"




params_get = {"api_key" : API_KEY, }
response_get = requests.get("https://api.challonge.com/v1/tournaments/999888999/participants.json",
                         headers={"User-Agent":user_agent},  params = params_get) #
print(response_get)

with sq.connect("../db.sqlite3") as con:
    cur = con.cursor()
    cur.execute("""SELECT nick FROM test WHERE id > 0""")
    result2 = cur.fetchmany(2)
    for i in result2:
        params_post = {"api_key": API_KEY, "participant[name]": i}
        response_post = requests.post("https://api.challonge.com/v1/tournaments/999888999/participants.json",
                                      headers={"User-Agent": user_agent}, params=params_post)
        print(response_post)
    












# challonge.set_credentials("ToMadeira", "ZpMMUqVouD83C40RQ67qItnnod5lPeAcDHa7Y7mL")
# tournament = challonge.tournaments.show(999888999)
#
# print(tournament["id"]) # 3272
# print(tournament["name"]) # My Awesome Tournament
# print(tournament["started_at"]) # None

