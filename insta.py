import instaloader

instagram = instaloader.Instaloader()
username = input("Enter username: ")
instagram.download_profile(username, profile_pic_only=True)

profile = instaloader.Profile.from_username(instagram.context, username)

private = profile.is_private
# print(private)

if not private:
    posts = list(profile.get_posts())
    latestPost = posts[0]
    instagram.download_post(latestPost, target=profile.username)
else:
    print("Account is Private, Can't access posts or private data")
    password = input("Enter your password: ")
    try:
        instagram.login(username, password)
        posts = list(profile.get_posts())
        latestPost = posts[0]
        instagram.download_post(latestPost, target=profile.username)
    except:
        print("Wrong Password!!")
