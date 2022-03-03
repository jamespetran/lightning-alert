import json
import math


def main():
    # init location_list as empty list type (var needs to be in this scope)
    location_list = []

    # init location dictionary
    location_dict = {}

    # init alerted dictionary
    alerted_asset = {}

    # assign json file of list of assets to location_list
    with open('./data/assets.json') as file:
        location_list = json.load(file)
        # convert list to dict, with key = quadKey and value = `${assetOwner}:${assetName}` to reduce time complexity from O(n^2) to O(n)
        # for location in location_list:
        


    # opens the file
    with open ('./data/lightning.json') as f:
        # for each separate line in file f:
        for json_obj in f:
            lightning_strike = json.loads(json_obj)
            # if lightning_strike is a heartbeat, then the alert is irrelevant and does not need to be posted
            # and the for loop should go onto the next value of lightning_strike
            if lightning_strike['flashType'] == 9:
                break

            # convert lat/long to quadKey
            # from https://docs.microsoft.com/en-us/bingmaps/articles/bing-maps-tile-system
            x = (lightning_strike["longitude"] + 180) / 360
            sin_long = math.sin(x)

            # iterate through the list of assets to see if lightning.quadKey == asset.quadKey

            # if yes, then
    
    # for lightning_strike in lightning_list:
    #     print(lightning_strike['receivedTime'])


main()
