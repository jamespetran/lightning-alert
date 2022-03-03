import json

def main():
    lightning_list = []

    with open ('./data/lightning.json') as f:
        for json_obj in f:
            lightning_strike = json.loads(json_obj)
            lightning_list.append(lightning_strike);
    
    print(lightning_list)


main()
