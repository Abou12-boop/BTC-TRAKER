import time
import urllib3
import requests
import datetime
import csv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Historie = []
argent = 10
btc_prix_achat = 0
btc_quantite = 0

def wallet():
    valeur_actuelle = btc_quantite * prix
    profit = valeur_actuelle - 1000
    profit_pct = (profit / 1000) * 100
    print("═" * 45)
    if btc_quantite != 0:
        print(f"💰 Solde      : {argent:.2f} $")
        print(f"₿  BTC        : {btc_quantite:.6f}")
        print(f"📈 Valeur     : {valeur_actuelle:.2f} $")
        print(f"🏷️  Acheté à  : {btc_prix_achat:.2f} $")
        print(f"💹 Profit     : {profit:.2f} $ ({profit_pct:.2f}%)")
    else:
        print(f"💰 Solde      : {argent:.2f} $")
        print(f"₿  BTC        : 0")
    print("═" * 45)

while True:
    api = requests.get("https://api.coinlore.net/api/ticker/?id=90", verify=False)
    donne = api.json()
    prix = float(donne[0]["price_usd"])
    time_now = datetime.datetime.now()

    Historie.append(prix)
    Historie = Historie[-20:]

    with open("BTC_storage.csv", "a", newline="") as fil:
        writer = csv.writer(fil)
        writer.writerow([time_now, prix])

    if len(Historie) >= 20:
        MA_court = sum(Historie[-5:]) / 5
        MA_long = sum(Historie[-20:]) / 20

        if MA_court > MA_long:
            print(f"📈 SIGNAL ACHAT | MA5: {MA_court:.2f} $ | MA20: {MA_long:.2f} $")
        else:
            print(f"📉 SIGNAL VENTE | MA5: {MA_court:.2f} $ | MA20: {MA_long:.2f} $")

        if MA_court > MA_long and btc_quantite == 0:
            btc_quantite = argent / prix
            btc_prix_achat = prix
            argent = 0
            print(f"✅ ACHAT ! {btc_quantite:.6f} BTC à {prix} $")

        if MA_court < MA_long and btc_quantite != 0:
            argent = btc_quantite * prix
            profit = argent - 1000
            btc_quantite = 0
            print(f"💰 VENTE ! Solde: {argent:.2f} $ | Profit: {profit:.2f} $")

        wallet()  # ✅ affiché à chaque tour

    else:
        print(f"Collecte des données... {len(Historie)}/20")

    time.sleep(10)



