def repeat(s, exclaim): 
    """
    docstring here.  describes function
    """

    result = s*3

    if exclaim:
        result = result + '!!!'

    return result


def main():
    print(repeat('Yay ', False))
    print(repeat('Woo Hoo ', True))

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
