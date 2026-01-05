def employee_status(experience_years,performance_score,is_team_player):
    if experience_years<0 or performance_score<0 or  performance_score>100:
        return "invalid"
    elif performance_score>=80 and experience_years>=5 and is_team_player:
        return "senior candidate"
    elif (performance_score >=70 or experience_years>=3) and is_team_player:
        return "strong candidate"
    else:
        return "average candidate"
cases=[(6,85,True),(4,75,True),(2,75,True),(7,90,False),(-1,80,True)]
results=[employee_status(e_y,p_s,is_t_p) for e_y,p_s,is_t_p in cases]
print(results)
