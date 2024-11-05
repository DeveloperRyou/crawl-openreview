import datetime

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
    review_content = review.content
    confidence_raw = review_content.get('confidence', '')
    correctness_raw = review_content.get('correctness', '')
    technical_novelty_and_significance_raw = review_content.get('technical_novelty_and_significance', '')
    empirical_novelty_and_significance_raw = review_content.get('empirical_novelty_and_significance', '')
    recommendation_raw = review_content.get('recommendation', '')

    confidence = confidence_raw.split(':')
    correctness = correctness_raw.split(':')
    technical_novelty_and_significance = technical_novelty_and_significance_raw.split(':')
    empirical_novelty_and_significance = empirical_novelty_and_significance_raw.split(':')
    recommendation = recommendation_raw.split(':')

    confidence_point = int(confidence[0]) if confidence and len(confidence) == 2 else None
    confidence_reasoning = confidence[1] if confidence and len(confidence) == 2  else None
    correctness_point = int(correctness[0]) if correctness and len(correctness) == 2 else None
    correctness_reasoning = correctness[1] if correctness and len(correctness) == 2 else None
    technical_novelty_and_significance_point = int(technical_novelty_and_significance[0]) if technical_novelty_and_significance and len(technical_novelty_and_significance) == 2 else None
    technical_novelty_and_significance_reasoning = technical_novelty_and_significance[1] if technical_novelty_and_significance and len(technical_novelty_and_significance) == 2 else None
    empirical_novelty_and_significance_point = int(empirical_novelty_and_significance[0]) if empirical_novelty_and_significance and len(empirical_novelty_and_significance) == 2 else None
    empirical_novelty_and_significance_reasoning = empirical_novelty_and_significance[1] if empirical_novelty_and_significance and len(empirical_novelty_and_significance) == 2 else None
    recommendation_point = int(recommendation[0]) if recommendation and len(recommendation) == 2 else None
    recommendation_reasoning = recommendation[1] if recommendation and len(recommendation) == 2 else None

    review_entity = {
        'id': review.id,
        'forum': review.forum,
        'confidence':  confidence_point,
        'confidence_reasoning': confidence_reasoning,
        'summary_of_the_paper': review_content.get('summary_of_the_paper', ''),
        'strength_and_weaknesses': review_content.get('strength_and_weaknesses', ''),
        'clarity_quality_novelty_and_reproducibility': review_content.get('clarity,_quality,_novelty_and_reproducibility', ''),
        'summary_of_the_review': review_content.get('summary_of_the_review', ''),
        'correctness': correctness_point,
        'correctness_reasoning': correctness_reasoning,
        'technical_novelty_and_significance': technical_novelty_and_significance_point,
        'technical_novelty_and_significance_reasoning': technical_novelty_and_significance_reasoning,
        'empirical_novelty_and_significance': empirical_novelty_and_significance_point,
        'empirical_novelty_and_significance_reasoning': empirical_novelty_and_significance_reasoning,
        'recommendation': recommendation_point,
        'recommendation_reasoning': recommendation_reasoning,
        'signatures': ', '.join(review.signatures),
        'invitation': review.invitation,
        'cdate': datetime.datetime.fromtimestamp(review.cdate / 1000)
    }
    return review_entity
