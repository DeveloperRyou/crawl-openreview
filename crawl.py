import openreview

def get_submissions(client, invitation):
    # 2023년 ICLR 컨퍼런스의 제출물
    submissions = list(openreview.tools.iterget_notes(
        client,
        invitation=invitation,
    ))
    print(f"초대정보 {invitation}의 제출물 수: {len(submissions)}")
    return submissions


def get_forum_dict(client, invitation):
    forum_dict = {}
    submissions = get_submissions(client, invitation)
    for submission in submissions:
        forum_dict[submission.forum] = submission
    print(f"초대정보 {invitation}의 포럼 수: {len(forum_dict)}")
    return forum_dict

def get_official_reviews(client, forum_id):
    reviews = []
    note_detail = list(openreview.tools.iterget_notes(
        client,
        forum=forum_id,
    ))
    for note in note_detail:
        if 'Official_Review' in note.invitation:
            reviews = reviews + [note]
    print(f"포럼 {forum_id}의 공식 리뷰 수: {len(reviews)}")
    return reviews