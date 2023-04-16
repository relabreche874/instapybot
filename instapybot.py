from instapy import InstaPy

session = InstaPy(username="test", password="test", want_check_browser=False).login()
# session = InstaPy(username="test", password="test", headless_browser=True, want_check_browser=False).login()
# headless_browser=True allows you to run the program from the command line
session.login()

session.like_by_tags(['bmw', 'mercedes'], amount=5)
session.set_dont_like(['nsfw', 'naked'])

session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)

session.set_do_comment(['Awesome!', 'Cool!', 'Radical'])

session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=10)
session.set_relationship_bounds(enabled=True, max_followers=300)

# session.set_use_clarifai(enabled=True, api_key='<your_api_key>')
# session.clarifai_check_img_for(['nsfw'])
# use clarifai to avoid certain images using AI

session.end()
