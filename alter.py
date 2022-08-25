
from array import array


class string():

    def __init__(self, x):
        self.sentance = x


#####################################################
    def reverse(sentance):

        letters = []
        ind_lst = []

        final = ""

        for letter in sentance:
            letters.append(letter)
            
        x = (-1*len(letters)) + 1
            
        for number in range(x, 1):
            ind_lst.append(abs(number))
            
        for number in ind_lst:
            final = final + letters[number]

        return final


#####################################################
    def encode(sentance):

        numbers = ['5', '1', '7', '8', '6', '2', '0', '3', '9', '4']
        alphabet_string = "abcdefghijklmnopqrstuvwxyz"
        alphabet = []
        special_charecters = '!@#$%^&*()_+|}{":?><'
        special = []

        for letter in alphabet_string:
            alphabet.append(letter)

        for letter in special_charecters:
            special.append(letter)

        sent = []
        final = ''

 
        for letter in sentance.lower():
            if letter in numbers:

                current_index = numbers.index(letter)
                sent.append(current_index)

            elif letter in alphabet:
                calc = len(alphabet) - (alphabet.index(letter) + 1)
                sent.append(alphabet[calc])
                

            elif letter in special:
                calc = abs(special.index(letter) - 1)
                sent.append(special[calc])

            else:
                sent.append(letter)

        for letter in sent:
            final = final + str(letter)

        return final


#####################################################
    def decode(sentance):

        numbers = ['5', '1', '7', '8', '6', '2', '0', '3', '9', '4']
        alphabet_string = "abcdefghijklmnopqrstuvwxyz"
        alphabet = []
        special_charecters = '!@#$%^&*()_+|}{":?><'
        special = []

        for letter in alphabet_string:
            alphabet.append(letter)

        for letter in special_charecters:
            special.append(letter)

        sent = []
        final = ''

        for letter in sentance:
            if letter in numbers:

                
                sent.append(numbers[int(letter)])

            elif letter in alphabet:
                index = len(alphabet) - (alphabet.index(letter) + 1)
                sent.append(alphabet[index])
                

            elif letter in special:
                calc = abs(special.index(letter) + 1)
                sent.append(special[calc])

            else:
                sent.append(letter)

        for letter in sent:
            final = final + str(letter)

        return final



class list():


    def __init__(self, list):
        self.list = list


#####################################################    
    def majority(list):

        string_count = 0
        int_count = 0
        bool_count = 0

        result = []

        for data_type in list:

            if isinstance(data_type, str) == True:
                string_count += 1

            elif isinstance(data_type, bool):
                bool_count += 1

            elif isinstance(data_type, int) == True:
                int_count += 1



        if string_count > bool_count and string_count > int_count:
            result.append("String")
            result.append(string_count)
                    

        elif int_count > bool_count and int_count > string_count:
            result.append("Integar")
            result.append(int_count)
                    

        elif bool_count > int_count and bool_count > string_count:
            result.append("Boolean")
            result.append(bool_count)

                    
        else:
            result.append("TIE")
            result.append("Integer {}".format(int_count))
            result.append("String: {}".format(string_count))
            result.append("Boolean: {}".format(bool_count))

        return result


#####################################################
    def substitute(list, from_, to):

        final = []

        for letter in list:
            if letter == from_:
                final.append(to)

            else:
                final.append(letter)

        
        return final


#####################################################   
    def remove_element(x, remove):

        final = []

        ds = [323, 23423]

        type_da = type(ds)

        if type(x) == type_da:
            for element in x:
                if str(element) in str(remove):
                    ds = "ds"

                else:
                    final.append(element)

        else:
                
            for element in x:
                if str(element) == str(remove):
                    c = "dsf"

                else:
                    final.append(element)

        return final