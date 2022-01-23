import sys
import subprocess
import os

def get_list(index: int, accept: list):
    accept = list(accept)
    accept[0], accept[index] = accept[index], accept[0]
    return accept

def generate_words(accept: list, col=0, row=0, text_list=[]):
    max = len(accept)

    if col == len(accept):
        col = 0
        row += 1
    if row == max:
        return list(set(text_list))
    if len(text_list) == row:
        text_list.append('')
    new_list = get_list(row, accept)
    text_list[row] += new_list[col]
    col += 1
    return generate_words(accept, col, row, text_list)

def domains_list(accept: list): 
    domains = generate_words(accept)
    domains = map(lambda x: x + ".ir", domains)
    return list(domains)

def check_domain(domainName: str):
    l = str(subprocess.check_output(["whois", domainName]))
    if "error" in l.lower():
        print(domainName, "available") 
        return domainName
    print(domainName, 'unavailable')
    return False

def check_domains(domains: list, index = 0):
    domain = domains[index]
    index += 1
    check_domain(domain)
    if len(domains) == index:
        return
    return check_domains(domains, index)


def  main():
    argv = sys.argv
    stdin = list(map(lambda x: x.strip(), sys.stdin))

    if len(argv) > 1:
        chars = argv[1]
    elif len(stdin) > 0:
        chars = stdin[0]
    else:
        chars = list(input('Enter words you want create domain name: '))
    v = domains_list((chars))
    check_domains(list(v))

if __name__ == '__main__':
    main()
