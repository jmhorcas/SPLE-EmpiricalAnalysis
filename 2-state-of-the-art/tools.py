import csv


PHASE = 'Which SPL phases support the tool?'
TYPE = 'Type of tool'
AVAILABLE = 'Is the tool available online to download/use?'
USABLE = 'Is the tool working well and/or usable?'

DA = '(DA)'
RA = '(RA)'
DI = '(DI)'
PD = '(PD)'

COMMERCIAL = 'Commercial'
CASE_TOOL = 'CASE Tool'
ACADEMIC = 'Academic'
PROTOTYPE = 'Prototype'

YES = 'Yes'
NO = 'No'


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

    print('==========')

    da_commercial = [x for x in total_da if COMMERCIAL in x[TYPE]]
    da_prototype = [x for x in total_da if PROTOTYPE in x[TYPE]]
    da_academic = [x for x in total_da if ACADEMIC in x[TYPE] or (x not in da_commercial and x not in da_prototype)]

    print(f'DA academic: {len(da_academic)} ({round(len(da_academic)/len(total_da)*100, 2)}%)')
    print(f'DA commercial: {len(da_commercial)} ({round(len(da_commercial)/len(total_da)*100, 2)}%)')
    print(f'DA prototype: {len(da_prototype)} ({round(len(da_prototype)/len(total_da)*100, 2)}%)')
    
    print('----------')

    ra_commercial = [x for x in total_ra if COMMERCIAL in x[TYPE]]
    ra_prototype = [x for x in total_ra if PROTOTYPE in x[TYPE]]
    ra_academic = [x for x in total_ra if ACADEMIC in x[TYPE] or (x not in ra_commercial and x not in ra_prototype)]

    print(f'RA academic: {len(ra_academic)} ({round(len(ra_academic)/len(total_ra)*100, 2)}%)')
    print(f'RA commercial: {len(ra_commercial)} ({round(len(ra_commercial)/len(total_ra)*100, 2)}%)')
    print(f'RA prototype: {len(ra_prototype)} ({round(len(ra_prototype)/len(total_ra)*100, 2)}%)')

    print('----------')

    di_commercial = [x for x in total_di if COMMERCIAL in x[TYPE]]
    di_prototype = [x for x in total_di if PROTOTYPE in x[TYPE]]
    di_academic = [x for x in total_di if ACADEMIC in x[TYPE] or (x not in di_commercial and x not in di_prototype)]

    print(f'DI academic: {len(di_academic)} ({round(len(di_academic)/len(total_di)*100, 2)}%)')
    print(f'DI commercial: {len(di_commercial)} ({round(len(di_commercial)/len(total_di)*100, 2)}%)')
    print(f'DI prototype: {len(di_prototype)} ({round(len(di_prototype)/len(total_di)*100, 2)}%)')

    print('----------')

    pd_commercial = [x for x in total_pd if COMMERCIAL in x[TYPE]]
    pd_prototype = [x for x in total_pd if PROTOTYPE in x[TYPE]]
    pd_academic = [x for x in total_pd if ACADEMIC in x[TYPE] or (x not in pd_commercial and x not in pd_prototype)]

    print(f'PD academic: {len(pd_academic)} ({round(len(pd_academic)/len(total_pd)*100, 2)}%)')
    print(f'PD commercial: {len(pd_commercial)} ({round(len(pd_commercial)/len(total_pd)*100, 2)}%)')
    print(f'PD prototype: {len(pd_prototype)} ({round(len(pd_prototype)/len(total_pd)*100, 2)}%)')

    print('----------')

    all_commercial = [x for x in da_ra_di_pd if COMMERCIAL in x[TYPE]]
    all_prototype = [x for x in da_ra_di_pd if PROTOTYPE in x[TYPE]]
    all_academic = [x for x in da_ra_di_pd if ACADEMIC in x[TYPE] or (x not in all_commercial and x not in all_prototype)]

    print(f'ALL academic: {len(all_academic)} ({round(len(all_academic)/len(da_ra_di_pd)*100, 2)}%)')
    print(f'ALL commercial: {len(all_commercial)} ({round(len(all_commercial)/len(da_ra_di_pd)*100, 2)}%)')
    print(f'ALL prototype: {len(all_prototype)} ({round(len(all_prototype)/len(da_ra_di_pd)*100, 2)}%)')
    
    print('==========AVAILABLE AND USABLE:')

    total_da = [x for x in total_da if YES in x[AVAILABLE] and YES in x[USABLE]]
    total_ra = [x for x in total_ra if YES in x[AVAILABLE] and YES in x[USABLE]]
    total_di = [x for x in total_di if YES in x[AVAILABLE] and YES in x[USABLE]]
    total_pd = [x for x in total_pd if YES in x[AVAILABLE] and YES in x[USABLE]]
    da_ra_di_pd = [x for x in da_ra_di_pd if YES in x[AVAILABLE] and YES in x[USABLE]]

    da_commercial = [x for x in total_da if COMMERCIAL in x[TYPE]]
    da_prototype = [x for x in total_da if PROTOTYPE in x[TYPE]]
    da_academic = [x for x in total_da if ACADEMIC in x[TYPE] or (x not in da_commercial and x not in da_prototype)]

    print(f'DA academic: {len(da_academic)} ({round(len(da_academic)/len(total_da)*100, 2)}%)')
    print(f'DA commercial: {len(da_commercial)} ({round(len(da_commercial)/len(total_da)*100, 2)}%)')
    print(f'DA prototype: {len(da_prototype)} ({round(len(da_prototype)/len(total_da)*100, 2)}%)')
    
    print('----------')

    ra_commercial = [x for x in total_ra if COMMERCIAL in x[TYPE]]
    ra_prototype = [x for x in total_ra if PROTOTYPE in x[TYPE]]
    ra_academic = [x for x in total_ra if ACADEMIC in x[TYPE] or (x not in ra_commercial and x not in ra_prototype)]

    print(f'RA academic: {len(ra_academic)} ({round(len(ra_academic)/len(total_ra)*100, 2)}%)')
    print(f'RA commercial: {len(ra_commercial)} ({round(len(ra_commercial)/len(total_ra)*100, 2)}%)')
    print(f'RA prototype: {len(ra_prototype)} ({round(len(ra_prototype)/len(total_ra)*100, 2)}%)')

    print('----------')

    di_commercial = [x for x in total_di if COMMERCIAL in x[TYPE]]
    di_prototype = [x for x in total_di if PROTOTYPE in x[TYPE]]
    di_academic = [x for x in total_di if ACADEMIC in x[TYPE] or (x not in di_commercial and x not in di_prototype)]

    print(f'DI academic: {len(di_academic)} ({round(len(di_academic)/len(total_di)*100, 2)}%)')
    print(f'DI commercial: {len(di_commercial)} ({round(len(di_commercial)/len(total_di)*100, 2)}%)')
    print(f'DI prototype: {len(di_prototype)} ({round(len(di_prototype)/len(total_di)*100, 2)}%)')

    print('----------')

    pd_commercial = [x for x in total_pd if COMMERCIAL in x[TYPE]]
    pd_prototype = [x for x in total_pd if PROTOTYPE in x[TYPE]]
    pd_academic = [x for x in total_pd if ACADEMIC in x[TYPE] or (x not in pd_commercial and x not in pd_prototype)]

    print(f'PD academic: {len(pd_academic)} ({round(len(pd_academic)/len(total_pd)*100, 2)}%)')
    print(f'PD commercial: {len(pd_commercial)} ({round(len(pd_commercial)/len(total_pd)*100, 2)}%)')
    print(f'PD prototype: {len(pd_prototype)} ({round(len(pd_prototype)/len(total_pd)*100, 2)}%)')

    print('----------')

    all_commercial = [x for x in da_ra_di_pd if COMMERCIAL in x[TYPE]]
    all_prototype = [x for x in da_ra_di_pd if PROTOTYPE in x[TYPE]]
    all_academic = [x for x in da_ra_di_pd if ACADEMIC in x[TYPE] or (x not in all_commercial and x not in all_prototype)]

    print(f'ALL academic: {len(all_academic)} ({round(len(all_academic)/len(da_ra_di_pd)*100, 2)}%)')
    print(f'ALL commercial: {len(all_commercial)} ({round(len(all_commercial)/len(da_ra_di_pd)*100, 2)}%)')
    print(f'ALL prototype: {len(all_prototype)} ({round(len(all_prototype)/len(da_ra_di_pd)*100, 2)}%)')

if __name__ == "__main__":
    main()
    
    
    