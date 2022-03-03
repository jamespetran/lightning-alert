import json
from pyquadkey2 import quadkey


def main():
    # init location_list as empty list type (var needs to be in this scope)
    asset_list = []

    # init location dictionary
    location_dict = {}

    # init alerted dictionary
    alerted_asset = {}

    map_zoom = 12

    def issue_alert(owner, name, quad_key):
        if quad_key in alerted_asset.keys():
            return

        

    # assign json file of list of assets to location_list
    with open('./data/assets.json') as file:
        asset_list = json.load(file)
        for asset in asset_list:
            # print(asset["quadKey"])
            pass
        # convert list to dict, with key = quadKey and value = `${assetOwner}:${assetName}` to reduce time complexity from O(n^2) to O(n)
        # for asset in asset_list:

    # opens the file
    with open('./data/lightning.json') as f:
        # for each separate line in file f:
        for json_obj in f:
            lightning_strike = json.loads(json_obj)
            # if lightning_strike is a heartbeat, then the alert is irrelevant and does not need to be posted
            # and the for loop should go onto the next value of lightning_strike
            if lightning_strike['flashType'] == 9:
                break
            # assign lat, long to x, y
            x, y = lightning_strike['latitude'], lightning_strike['longitude']
            # calculate quadkey for given lat/long
            lightning_qk = quadkey.from_geo((x, y), map_zoom)
            # iterate through asset list to compare quadkeys
            for asset in asset_list:
                if (asset['quadKey'] == lightning_qk):
                    issue_alert(asset["assetOwner"], asset["assetName"], lightning_qk)


main()
