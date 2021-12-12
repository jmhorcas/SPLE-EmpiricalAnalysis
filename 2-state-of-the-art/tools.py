import csv


DA = '(DA)'
RA = '(RA)'
DI = '(DI)'
PD = '(PD)'
PHASE = 'Which SPL phases support the tool?'

def get_data(filepath: str) -> tuple[list[str], list[dict[str, str]]]:
    data = []
    headers = []
    with open(filepath, encoding='utf8', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',', skipinitialspace=True, quotechar='"')
        headers = csv_reader.fieldnames
        for row in csv_reader:
            data.append(row)
    return (headers, data)


def main():
    headers, data = get_data('tools.csv')

    n = len(data)
    total_da = [x for x in data if DA in x[PHASE]]
    total_ra = [x for x in data if RA in x[PHASE]]
    total_di = [x for x in data if DI in x[PHASE]] 
    total_pd = [x for x in data if PD in x[PHASE]] 
    #
    only_da = [x for x in total_da if RA not in x[PHASE] and DI not in x[PHASE] and PD not in x[PHASE]]
    only_ra = [x for x in total_ra if DA not in x[PHASE] and DI not in x[PHASE] and PD not in x[PHASE]]
    only_di = [x for x in total_di if DA not in x[PHASE] and RA not in x[PHASE] and PD not in x[PHASE]]
    only_pd = [x for x in total_pd if DA not in x[PHASE] and RA not in x[PHASE] and DI not in x[PHASE]]
    #
    da_ra = [x for x in data if DA in x[PHASE] and RA in x[PHASE] and DI not in x[PHASE] and PD not in x[PHASE]]
    da_di = [x for x in data if DA in x[PHASE] and DI in x[PHASE] and RA not in x[PHASE] and PD not in x[PHASE]]
    da_pd = [x for x in data if DA in x[PHASE] and PD in x[PHASE] and RA not in x[PHASE] and DI not in x[PHASE]]

    ra_di = [x for x in data if RA in x[PHASE] and DI in x[PHASE] and DA not in x[PHASE] and PD not in x[PHASE]]
    ra_pd = [x for x in data if RA in x[PHASE] and PD in x[PHASE] and DA not in x[PHASE] and DI not in x[PHASE]]

    di_pd = [x for x in data if DI in x[PHASE] and PD in x[PHASE] and DA not in x[PHASE] and RA not in x[PHASE]]
    #
    da_ra_di = [x for x in data if DA in x[PHASE] and RA in x[PHASE] and DI in x[PHASE] and PD not in x[PHASE]]
    da_ra_pd = [x for x in data if DA in x[PHASE] and RA in x[PHASE] and PD in x[PHASE] and DI not in x[PHASE]]
    da_di_pd = [x for x in data if DA in x[PHASE] and DI in x[PHASE] and PD in x[PHASE] and RA not in x[PHASE]]
    ra_di_pd = [x for x in data if RA in x[PHASE] and DI in x[PHASE] and PD in x[PHASE] and DA not in x[PHASE]]
    #
    da_ra_di_pd = [x for x in data if DA in x[PHASE] and RA in x[PHASE] and DI in x[PHASE] and PD in x[PHASE]]

    print(f'only DA: {len(only_da)} ({round(len(only_da)/n*100, 2)}%)')
    print(f'only RA: {len(only_ra)} ({round(len(only_ra)/n*100, 2)}%)')
    print(f'only DI: {len(only_di)} ({round(len(only_di)/n*100, 2)}%)')
    print(f'only PD: {len(only_pd)} ({round(len(only_pd)/n*100, 2)}%)')
    print('----------')
    print(f'DA + RA: {len(da_ra)} ({round(len(da_ra)/n*100, 2)}%)')
    print(f'DA + DI: {len(da_di)} ({round(len(da_di)/n*100, 2)}%)')
    print(f'DA + PD: {len(da_pd)} ({round(len(da_pd)/n*100, 2)}%)')
    print('-----')
    print(f'RA + DI: {len(ra_di)} ({round(len(ra_di)/n*100, 2)}%)')
    print(f'RA + PD: {len(ra_pd)} ({round(len(ra_pd)/n*100, 2)}%)')
    print('-----')
    print(f'DI + PD: {len(di_pd)} ({round(len(di_pd)/n*100, 2)}%)')
    print('----------')
    print(f'DA + RA + DI: {len(da_ra_di)} ({round(len(da_ra_di)/n*100, 2)}%)')
    print(f'DA + RA + PD: {len(da_ra_pd)} ({round(len(da_ra_pd)/n*100, 2)}%)')
    print(f'DA + DI + PD: {len(da_di_pd)} ({round(len(da_di_pd)/n*100, 2)}%)')
    print(f'RA + DI + PD: {len(ra_di_pd)} ({round(len(ra_di_pd)/n*100, 2)}%)')
    print('----------')
    print(f'DA + RA + DI + PD: {len(da_ra_di_pd)} ({round(len(da_ra_di_pd)/n*100, 2)}%)')
    print('----------')
    print('----------')
    print(f'DA: {len(total_da)} ({round(len(total_da)/n*100, 2)}%)')
    print(f'RA: {len(total_ra)} ({round(len(total_ra)/n*100, 2)}%)')
    print(f'DI: {len(total_di)} ({round(len(total_di)/n*100, 2)}%)')
    print(f'PD: {len(total_pd)} ({round(len(total_pd)/n*100, 2)}%)')


    for t in only_pd:
        print(t['Tool name'])
    

if __name__ == "__main__":
    main()
    
    