
def getRank(filename, name, gender):
    with open(filename, 'r') as lof:
        lines = lof.readlines()
        for line in lines:
            values = line.split('\t')
            if gender == 1:
                if len(values) > 1 and values[1] == name:
                    rank = values[0]
                    return rank
                else:
                    pass
            if gender == 2:
                if values[-2] == name:
                    rank = values[0]
                    return rank
                else:
                    pass
    return "Not ranked"

if __name__ == '__main__':
    name = input("Enter the baby name you wish to research:  \n")
    namesearching = name.title()
    gender = int(input("Which gender list do you wish to research?\n1.  Male\n2.  Female\nEnter selection:  "))
    while gender != 1 and gender != 2:
        gender = int(input("ERROR:  must enter a 1 or a 2\nPlease re-enter:"))
    else:
        pass
    print(f'For name:  {namesearching}\nDecade Rank\n======  ==========')
    ninteenhunnid = getRank('NamesOf1900s.txt', namesearching, gender)
    ninteenhunnidone = getRank('NamesOf1910s.txt', namesearching, gender)
    ninteenhunnidtwo = getRank('NamesOf1920s.txt', namesearching, gender)
    ninteenhunnidthree = getRank('NamesOf1930s.txt', namesearching, gender)
    ninteenhunnidfour = getRank('NamesOf1940s.txt', namesearching, gender)
    ninteenhunnidfive = getRank('NamesOf1950s.txt', namesearching, gender)
    ninteenhunnidsix = getRank('NamesOf1960s.txt', namesearching, gender)
    ninteenhunnidseven = getRank('NamesOf1970s.txt', namesearching, gender)
    ninteenhunnideight = getRank('NamesOf1980s.txt', namesearching, gender)
    ninteenhunnidnine = getRank('NamesOf1990s.txt', namesearching, gender)
    print(f'1900\t{ninteenhunnid}')
    print(f'1910\t{ninteenhunnidone}')
    print(f'1920\t{ninteenhunnidtwo}')
    print(f'1930\t{ninteenhunnidthree}')
    print(f'1940\t{ninteenhunnidfour}')
    print(f'1950\t{ninteenhunnidfive}')
    print(f'1960\t{ninteenhunnidsix}')
    print(f'1970\t{ninteenhunnidseven}')
    print(f'1980\t{ninteenhunnideight}')
    print(f'1990\t{ninteenhunnidnine}')
