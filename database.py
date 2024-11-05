import mysql.connector

def create_db():
    # MySQL 데이터베이스 연결 설정
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='openreview_db' 
    )

    cursor = db.cursor()

    # forum 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS forum (
        id VARCHAR(255) NOT NULL PRIMARY KEY,
        title TEXT NOT NULL,
        abstract TEXT NOT NULL,
        authors TEXT NOT NULL,
        keywords TEXT NOT NULL,
        pdf VARCHAR(255) NOT NULL,
        invitation VARCHAR(255) NOT NULL,
        cdate TIMESTAMP NOT NULL
    )
    """)

    # review 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS review (
        id VARCHAR(255) NOT NULL PRIMARY KEY,
        forum VARCHAR(255) NOT NULL,
        confidence INT,
        confidence_reasoning TEXT,
        summary_of_the_paper TEXT,
        strength_and_weaknesses TEXT,
        clarity_quality_novelty_and_reproducibility TEXT,
        summary_of_the_review TEXT,
        correctness INT,
        correctness_reasoning TEXT,
        technical_novelty_and_significance INT,
        technical_novelty_and_significance_reasoning TEXT,
        empirical_novelty_and_significance INT,
        empirical_novelty_and_significance_reasoning TEXT,
        recommendation INT,
        recommendation_reasoning TEXT,
        signatures VARCHAR(255) NOT NULL,
        invitation VARCHAR(255) NOT NULL,
        cdate TIMESTAMP NOT NULL,
        FOREIGN KEY (forum) REFERENCES forum(id)
    )
    """)

    return db, cursor

def insert_forum(db, cursor, forum_entity):
    # forum 데이터 삽입
    try:
        cursor.execute("""
        INSERT INTO forum (id, title, abstract, authors, keywords, pdf, invitation, cdate)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            forum_entity['id'],
            forum_entity['title'],
            forum_entity['abstract'],
            forum_entity['authors'],
            forum_entity['keywords'],
            forum_entity['pdf'],
            forum_entity['invitation'],
            forum_entity['cdate']
        ))
        db.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()

def insert_review(db, cursor, review_entity):
    # review 데이터 삽입
    try:
        cursor.execute("""
        INSERT INTO review (id, forum, 
                       confidence, confidence_reasoning, summary_of_the_paper, 
                       strength_and_weaknesses, clarity_quality_novelty_and_reproducibility, summary_of_the_review, 
                       correctness, correctness_reasoning, 
                       technical_novelty_and_significance, technical_novelty_and_significance_reasoning, 
                       empirical_novelty_and_significance, empirical_novelty_and_significance_reasoning, 
                       recommendation, recommendation_reasoning, 
                       signatures, invitation, cdate)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            review_entity['id'],
            review_entity['forum'],
            review_entity['confidence'],
            review_entity['confidence_reasoning'],
            review_entity['summary_of_the_paper'],
            review_entity['strength_and_weaknesses'],
            review_entity['clarity_quality_novelty_and_reproducibility'],
            review_entity['summary_of_the_review'],
            review_entity['correctness'],
            review_entity['correctness_reasoning'],
            review_entity['technical_novelty_and_significance'],
            review_entity['technical_novelty_and_significance_reasoning'],
            review_entity['empirical_novelty_and_significance'],
            review_entity['empirical_novelty_and_significance_reasoning'],
            review_entity['recommendation'],
            review_entity['recommendation_reasoning'],
            review_entity['signatures'],
            review_entity['invitation'],
            review_entity['cdate']
        ))
        db.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
