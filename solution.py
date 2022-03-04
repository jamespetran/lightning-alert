import json
from pyquadkey2 import quadkey


def main():
    # init location_list as empty list type (var needs to be in this scope)
    asset_list = []

    # init location dictionary
    asset_dict = {}

    # init alerted dictionary
    alerted_asset = {}

    # supplied map zoom level in instructions (12) to generate quadKey from lat, long
    map_zoom = 12

    # assign json file of list of assets to asset_list
    with open('./data/assets.json') as file:
        # asset_list = json.load(file)
        # convert list to dict, with key == quadKey and value == `${assetOwner}:${assetName}` to reduce time
        # complexity from O(n^2) to O(n + m) where n == lightning list and m == asset list => simplifies to O(n)
        for asset in json.load(file):
            # print(asset["quadKey"])
            owner, name, location = asset["assetOwner"], asset["assetName"], asset['quadKey']
            # store asset details so the alert can go out as required in instructions
            # ``` lightning alert for <assetOwner>:<assetName> ```
            asset_dict[location] = str(owner) + ":" + str(name)
            # print(asset_dict[location])

            # output of this with open... fx will result in a location_dict full of all of the assets that must be tracked

    # opens the lightning strike file as f
    with open('./data/lightning.json') as f:
        # run thru each separate line in file f:
        for json_obj in f:
            # assign this json_obj to new lightning strike (parsing the single json_obj as a string)
            lightning_strike = json.loads(json_obj)
            # if lightning_strike is a heartbeat, then the alert is irrelevant and does not need to be displayed
            # and the for loop should go onto the next lightning_strike in f
            if lightning_strike['flashType'] == 9:
                continue
            # assign lat, long to x, y
            x, y = lightning_strike['latitude'], lightning_strike['longitude']
            # calculate lightning quadkey from lightning strike lat/long using pyquadkey2's quadkey.from_geo()
            lightning_qk = quadkey.from_geo((x, y), map_zoom)
            # turn qk into string so we can compare them
            lightning_qk = str(lightning_qk)
            # is the lightning strike near a monitored asset?
            # is lightning_qk present in asset_dict{} ?
            if lightning_qk in asset_dict:
                # has alert already been called for this asset?
                # or... is asset already in alerted_asset{} ?
                if lightning_qk in alerted_asset:
                    # don't send an alert and then continue onto the next json_obj in f
                    continue

                else:
                    # add this quadkey to the alerted_asset dictionary so we don't send another alert after this one
                    alerted_asset[lightning_qk] = str(owner) + ":" + str(name)
                
                # alerted_asset[str]
                print("alert in "+ str(asset_dict[lightning_qk]))
    

            # will refactor this above 👆
            # loop through asset list to compare quadkeys to check if a match
            # for asset in asset_list:
            #     # check the asset given quadkey compared to the lightning strike 
            #     # calculated quadkey from lat/long
            #     if (asset['quadKey'] == str(lightning_qk)):
            #         # assign to easier to use vars
            #         owner, name, location = asset["assetOwner"], asset["assetName"], asset['quadKey']
            #         # check if this quadkey has had a prev alert (check if the quadkey has previously been stored in the alerted_asset dict)
            #         if location in alerted_asset:
            #             # then skip issuing an alert and continue onto the next asset in asset_list
            #             continue
            #         else:
            #             # add this quadkey to the alerted_asset dictionary
            #             alerted_asset[location] = str(owner) + ":" + str(name)
            #         # alerted_asset[str]
            #         print("alert in " + owner + ":" + name)


main()
