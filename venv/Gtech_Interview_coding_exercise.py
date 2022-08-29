# How would you get the company with the highest SAT score average, given a CSV file with an individual's name, his/her company and his/her SAT score?
# Data from CSV file already in iterable object of my choice

def highest_avg_sat_score():
    
    sat_scores_list = [{name:"john", company:"google", sat:100)}, {name:"bot", company:"amazon", sat:95}, {name:"todd", company:"microsoft", sat:96}]
    
    res_map = {}
    
    res_map_count = {}
    
    
    for sat_map in sat_scores_list:

       company = sat_map[company]

       res_map[company] = get(res_map[company], 0) + sat_map[sat]

       res_map_count[company] = get(res_map_count[company], 0) + 1

    res_list = sorted(res_map.items(), key=lambda x:x[1], reverse=True)

    return res_list[0][1] / res_map_count[res_list[0][0]]