import json

def main():
    # init lightning_list as empty list type
    lightning_list = []

    # opens the file
    with open ('./data/lightning.json') as f:
        # for each line in file f:
        for json_obj in f:
            # lightning strike is 
            lightning_strike = json.loads(json_obj)
            lightning_list.append(lightning_strike)
    
    # print(lightning_list[0])
    for lightning_strike in lightning_list:
        print(lightning_strike['receivedTime'])

    # location_list = []

    # location_list = json.load('./data/assets.json')
    # print(location_list)


main()
