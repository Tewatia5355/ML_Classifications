import base64
from github import Github
username = "Tewatia5355"
g = Github()
user = g.get_user(username)
proj = []
for repo in user.get_repos():
    proj.append(repo.name)

print(proj)

@application.route("/gitt/", methods=["POST"])
def repoo():
    import base64
    from github import Github
    username = "Tewatia5355"
    g = Github()
    user = g.get_user(username)
    proj = []
    for repo in user.get_repos():
        proj.append(repo.name)
    return jsonify(proj)