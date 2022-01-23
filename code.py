import sys
import subprocess
import os

FAIL_COLOR='\033[91m'
BOLD_COLOR='\033[1m'
END_COLOR='\033[0m'
OK_COLOR='\033[96m'

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
    print(BOLD_COLOR + domainName + END_COLOR, end=' ')
    if "error" in l.lower():
        print(OK_COLOR + "available" + END_COLOR) 
        return domainName
    print(FAIL_COLOR +  'unavailable', END_COLOR)
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

    if len(argv) > 1:
        chars = argv[1]
    else:
        chars = list(input())
    if len(chars) < 3:
        print(FAIL_COLOR + "Enter 3 words or more" + END_COLOR)
        return
    v = domains_list((chars))
    check_domains(list(v))

if __name__ == '__main__':
    main()
