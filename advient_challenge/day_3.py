import re
import requests
import os





def get_source() -> str:
    # URL de la página
    url = "https://adventofcode.com/2024/day/3/input"

    # Realizar solicitud HTTP

    session = os.getenv("SESSION")
    cookies = {'session': session}

    response = requests.get(url, cookies=cookies)
    return response.text


def get_results_of_mul(list_mul:list[str]):
    multiply: list[int] = []
    res_multipy: int = 1
    res_sum: int = 0
    rgx = r'\d+'
    for li in list_mul:
        cadena = re.findall(rgx, li)
        print("the second string is", cadena)
        cadena_int = [int(x) for x in cadena]
        print("the int list is", cadena_int)
        for cad in cadena_int:
            res_multipy *= cad
        
        multiply.append(res_multipy)
        res_multipy = 1


    print("the total multiplications are", multiply)

    for mult in multiply:
        res_sum += mult

    print("sum_total", res_sum)

    

    return res_sum
            





if __name__ == "__main__":
    #input_text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    input_text = get_source()
    print(input_text)


rgx = r'mul\(\d+,\d+\)'
cadena = re.findall(rgx, input_text)
get_results_of_mul(cadena)
#print("the chain is",cadena) 

