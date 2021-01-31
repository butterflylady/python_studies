from operator import itemgetter

import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

"""
First, we make an API call, and then print the status of the response.
This API call returns a list containing the IDs of up to the 500 most popular
articles on Hacker News at the time the call is issued. We then convert
the response object to a Python list, which we store in submission_ids.
We’ll use these IDs to build a set of dictionaries that each store information
about one of the current submissions.
We set up an empty list called submission_dicts to store these dictionaries.
We then loop through the IDs of the top 30 submissions. We make a
new API call for each submission by generating a URL that includes the current
value of submission_id. We print the status of each request along with
its ID, so we can see whether it’s successful.
We create a dictionary for the submission currently being processed,
where we store the title of the submission, a link to the discussion
page for that item, and the number of comments the article has received so
far. Then we append each submission_dict to the list submission_dicts.
Each submission on Hacker News is ranked according to an overall
score based on a number of factors including how many times it’s been
voted up, how many comments it’s received, and how recent the submission
is. We want to sort the list of dictionaries by the number of comments.
To do this, we use a function called itemgetter(), which comes from the
operator module. We pass this function the key 'comments', and it pulls the
value associated with that key from each dictionary in the list. The sorted()
function then uses this value as its basis for sorting the list. We sort the list
in reverse order to place the most-commented stories first.
Once the list is sorted, we loop through the list and print out
three pieces of information about each of the top submissions: the title,
a link to the discussion page, and the number of comments the submission
currently has.
"""
