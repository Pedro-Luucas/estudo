def reverse(string):
    if string == '':
        return ''
    
    return reverse(string[1:]) + string[0]

print(reverse('paralelepipedo'))