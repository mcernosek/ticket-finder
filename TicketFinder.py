#!/usr/bin/python
import praw
import pdb
import os


# Create the Reddit instance. Imported from praw.ini
reddit = praw.Reddit('bot1')

# Get submission instance for specific thread based on ID (thread link below)
# https://www.reddit.com/r/aclfestival/comments/bjh8ca/official_2019_acl_festival_buyselltrade_ticket/
submission = reddit.submission(id='bjh8ca')

submission.comment_sort = 'new'
submission.comments.replace_more(limit=0)
seller_comments = submission.comments


for comment in seller_comments:
    # Find reddit post based on desired text strings
    if "selling" in comment.body.lower() and "saturday" in comment.body.lower(): 
        replies_to_seller = comment.replies
        already_commented = False

        for reply in replies_to_seller:
            if already_commented == True:
                break

            if "username" in reply.body.lower():
                already_commented = True 

        if already_commented == False:
            # Handles comment rate limit exception which will occurr 
            # if reddit account is not verified or does not have enough karma 
            try:
                comment.reply('Message incoming from /u/username')

            except:
                break