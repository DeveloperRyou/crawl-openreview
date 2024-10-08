import openreview
import database
import crawl
import factory

# OpenReview 클라이언트 생성
client = openreview.Client(
    baseurl='https://api.openreview.net',
    username='developerryou@gmail.com',
    password='DEVtjdals991*'
)

db, cursor = database.create_db()

invitations = [
    'ICLR.cc/2023/Conference/-/Blind_Submission',
    'ICLR.cc/2022/Conference/-/Blind_Submission',
    'ICLR.cc/2021/Conference/-/Blind_Submission',
    'ICLR.cc/2020/Conference/-/Blind_Submission',
    'ICLR.cc/2019/Conference/-/Blind_Submission',
    'ICLR.cc/2018/Conference/-/Blind_Submission',
    'ICLR.cc/2017/Conference/-/Blind_Submission',
    'ICLR.cc/2016/Conference/-/Blind_Submission',
    'ICLR.cc/2015/Conference/-/Blind_Submission',
    'ICLR.cc/2014/Conference/-/Blind_Submission',
    'ICLR.cc/2013/Conference/-/Blind_Submission'
]

def save_forum_review_to_db(invitation):
    # 포럼 ID 집합
    forum_dict = crawl.get_forum_dict(client, invitation)

    # 포럼에 대한 정보
    for forum_id in list(forum_dict):
        forum = forum_dict[forum_id]
        forum_entity = factory.convert_forum_to_forum_entity(forum)
        database.insert_forum(db, cursor, forum_entity)

        official_reviews = crawl.get_official_reviews(client, forum_id)
        for review in official_reviews:
            review_entity = factory.convert_review_to_review_entity(review)
            database.insert_review(db, cursor, review_entity)
        
        print(f"포럼 {forum_id}의 정보를 데이터베이스에 저장했습니다.")

for invitation in invitations:
    save_forum_review_to_db(invitation)