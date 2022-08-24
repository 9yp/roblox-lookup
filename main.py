
import requests
import json

target=input("Roblox User ID: ")
data=requests.get("https://users.roblox.com/v1/users/" + target).json()
display=data["displayName"]
username=data["name"]
description=data["description"]
banned=data["isBanned"]
verified=data["hasVerifiedBadge"]
created=data["created"][0:10]
followers = requests.get(f"https://friends.roblox.com/v1/users/{target}/followers/count").json()["count"]
following = requests.get(f"https://friends.roblox.com/v1/users/{target}/followings/count").json()["count"]
friends = requests.get(f"https://friends.roblox.com/v1/users/{target}/friends/count").json()["count"]
cursor = ""
badges = 0
while True:
  r=requests.get(f"https://badges.roblox.com/v1/users/{target}/badges?limit=100&cursor={cursor}").json()
  badges + len(r["data"])
  if r["nextPageCursor"] == None:
    break
  if cursor == r["nextPageCursor"]:
    break
  cursor = r["nextPageCursor"]
eggs=len(requests.get(f"https://api.ropro.io/getEggCollection.php?userid={target}").json()["data"])
ropro=requests.get(f"https://api.ropro.io/getUserInfoTest.php?userid={target}").json()
reputation=ropro["reputation"]
discord=ropro["discord"]
groups=len(requests.get(f"https://groups.roblox.com/v2/users/{target}/groups/roles").json()["data"])
data = f"""Username: {username}
Display Name: {display}
User ID: {target}
Description: {description}
Created: {created}
Banned: {banned}
Followers: {followers}
Following: {following}
Friends: {friends}
Badges: {badges}
Groups: {groups}
Verified Badge: {verified}
Ropro Eggs: {eggs}
Ropro Reputation: {reputation}
Discord: {discord}
"""
print(data)
