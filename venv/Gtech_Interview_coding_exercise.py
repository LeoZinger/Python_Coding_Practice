# How would you get the 'company' with the highest 'sat' score average, given a CSV file with an individual's 'name', his/her 'company' and his/her 'sat' score?
# Data from CSV file already in iterable object of my choice

def highest_avg_sat_score():
    sat_scores_list = [{'name':'john', 'company':'google', 'sat':100}, {'name':'bot', 'company':'amazon', 'sat':95},
    {'name':'todd', 'company':'microsoft', 'sat':96}]
    print("sat_scores_list = ", sat_scores_list[0])

    res_map = {}
    res_map_count = {}

    for sat_map in sat_scores_list:
        company_name = sat_map['company']
        print("company name = ", company_name)

        res_map_count[company_name] = res_map_count.get(company_name, 0) + 1

        res_map[company_name] = (res_map.get(company_name, 0) + sat_map['sat']) / res_map_count[company_name]
        print("res_map[", company_name, "] = ", res_map[company_name])
        print("res_map_count[", company_name, "] = ", res_map_count[company_name])

    res_list = sorted(res_map.items(), key=lambda x:x[1], reverse=True)

    return res_list[0][1]

print("highest_avg_sat_score = ", highest_avg_sat_score())