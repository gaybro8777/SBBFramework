import operator

list_scores =  [95.70833, 102.70833, 104.33333, 104.79166, 107.09375, 107.94791, 108.03125, 108.03125, 108.13541, 108.23958, 109.40625, 110.63541, 110.63541, 110.63541, 110.63541, 110.63541, 111.59375, 111.59375, 111.59375, 111.59375, 111.76041, 113.01041, 113.05208, 113.60416, 113.60416, 113.66666, 113.70833, 113.70833, 113.70833, 113.70833, 113.70833, 113.70833, 113.70833, 113.70833, 113.70833, 113.70833, 113.70833, 113.70833, 113.70833, 113.70833, 114.30208, 114.34375, 114.65625, 114.65625, 114.92708, 115.42708, 116.51041, 116.78124, 116.90624, 117.21875]
list_ids = ['(7601-148)', '(7534-146)', '(6528-127)', '(7053-137)', '(6366-123)', '(5967-116)', '(6419-124)', '(7541-146)', '(7626-148)', '(7653-149)', '(3235-62)', '(6850-133)', '(7618-148)', '(7218-140)', '(7596-147)', '(6835-133)', '(7663-149)', '(7299-142)', '(7381-143)', '(7692-149)', '(7612-148)', '(7409-144)', '(5983-116)', '(6456-125)', '(6658-129)', '(7281-141)', '(7650-149)', '(7581-147)', '(5156-100)', '(7223-140)', '(7682-149)', '(7666-149)', '(7550-147)', '(5546-107)', '(6653-129)', '(6953-135)', '(6787-132)', '(7327-142)', '(7545-146)', '(6975-135)', '(7694-149)', '(7248-141)', '(7579-147)', '(7472-145)', '(7662-149)', '(7664-149)', '(7536-146)', '(7361-143)', '(7608-148)', '(7670-149)']



previous_score = 0.0
best_teams = {}
for score, team_id in zip(list_scores, list_ids):
    score_improvement = score - previous_score
    if score_improvement > 0.75:
        best_teams[team_id] = score_improvement
    previous_score = score

rank = sorted(best_teams.items(), key=operator.itemgetter(1), reverse=True)
print "\n"+str(rank)
rank = [r[0] for r in rank]
print str(rank)+"\n"