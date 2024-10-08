import datetime
import json

def convert_forum_to_forum_entity(forum):
    forum_entity = {
        'id': forum.id,
        'title': forum.content.get('title', ''),
        'abstract': forum.content.get('abstract', ''),
        'authors': ', '.join(forum.content.get('authors', [])),
        'keywords': ', '.join(forum.content.get('keywords', [])),
        'pdf': 'https://openreview.net' + forum.content.get('pdf', ''),
        'invitation': forum.invitation,
        'cdate': datetime.datetime.fromtimestamp(forum.cdate / 1000)
    }
    return forum_entity

def convert_review_to_review_entity(review):
    review_entity = {
        'id': review.id,
        'forum': review.forum,
        'content': json.dumps(review.content),
        'signatures': ', '.join(review.signatures),
        'invitation': review.invitation,
        'cdate': datetime.datetime.fromtimestamp(review.cdate / 1000)
    }
    return review_entity