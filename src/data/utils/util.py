def fix_timeline(elementos:list, first_year:int, current_year:int):
    difference_in_years = current_year - first_year
    n_linhas = (difference_in_years*len(elementos))-difference_in_years
    if difference_in_years>0:
        for _ in range(n_linhas):
            elementos.insert(1, '')
    return elementos