#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas


# In[41]:


import matplotlib


# In[42]:


import random

def generate_random_number(minimum, maximum):
    if(minimum > maximum):
        return None
    return random.randint(minimum, maximum)
    
def generate_random_string(length, alphabet):
    if(alphabet == "" or alphabet == None):
        return None
    result_string = ""
    for i in range (0, length):
        result_string += random.choice(alphabet)
    return result_string

def choose_random_from_file(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    
    random_line = random.randrange(0, len(lines))
    
    return (lines[random_line]).strip()

def create_random_id(id_size: int, min_value: int, max_value: int):
    value_set = [str(i) for i in range(min_value, max_value+1)]

    result_id = []
    for i in range(id_size):
        if(len(value_set) == 0):
            break
        random_element = random.randrange(len(value_set))

        result_id.append(value_set[random_element])
        value_set.pop(random_element)

    
    return result_id


def generate_random_date():
    day = random.randint(1, 29)
    month = random.randint(1, 12)
    year = random.randint(2000, 2030)
    
    date = "{0:02}/{1:02}/{2}".format(day, month, year)
    return date


def create_random_address():
    orientations_north_south = ["Calle", "Diagonal"]
    orientations_west_easth = ["Carrera", "Transversal"]
    additions = ["A", "B", "C", "D", ""]
    
    first_addition = random.choice(additions)
    second_addition = random.choice(additions)
    
    is_south = random.choice(["", "Sur"])
    
    is_bis = random.choice(["bis", ""])
    if(second_addition == ""):
        is_bis = ""
    
    main_orientation = random.choice(orientations_north_south + orientations_west_easth)
    main_number = random.randint(1, 200)
    second_number = random.randint(1, 200)
    third_number = random.randint(1, 200)
    
    result_address = None
    format_string = ""
    
    if(main_orientation in orientations_north_south):
        format_string = "{orientation} {first}{first_addition} {isSouth} #{second}{second_addition}{bis}-{third}"
    else:
        format_string = "{orientation} {first}{first_addition} #{second}{second_addition}{bis}-{third} {isSouth}"
    return format_string.format(orientation = main_orientation, 
                              first = main_number, 
                              second = second_number,
                              third = third_number,
                              isSouth = is_south,
                              first_addition = first_addition,
                              second_addition = second_addition,
                              bis =  is_bis
                             )


# In[43]:


import unittest

class IntervalNumberTestClass(unittest.TestCase):
    
    def assert_number_in_interval(self, minumum, maximum, value):
        self.assertTrue(minumum <= value <= maximum)
    
    def test_should_get_unique_random(self):
        number = generate_random_number(100, 100)
        self.assertEquals(number, 100)
        
    def test_should_get_invalid_interval(self):
        number = generate_random_number(200, 100)
        self.assertEqual(number, None)
        
    def test_should_get_random(self):
        number = generate_random_number(0, 10)
        self.assert_number_in_interval(0, 10, number)
        
        number_2 = generate_random_number(0, 10)
        self.assert_number_in_interval(0, 10, number_2)
        
        number_3 = generate_random_number(0, 10)
        self.assert_number_in_interval(0, 10, number_3)
        
    
if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(IntervalNumberTestClass))


# In[44]:


import unittest

class RandomStringTestClass(unittest.TestCase):

    def test_should_get_empty_string(self):
        random_string = generate_random_string(0, "abc")
        self.assertEqual(0, len(random_string))
        
    def test_should_return_exact_length(self):
        random_string = generate_random_string(5, "abc")
        self.assertEqual(5, len(random_string))
        
        random_string = generate_random_string(10, "abc")
        self.assertEqual(10, len(random_string))
        
        random_string = generate_random_string(1000, "abc")
        self.assertEqual(1000, len(random_string))

    def test_should_use_alphabet(self):
        random_string = generate_random_string(5, "abc")
        self.assert_alphabet_use("abc", random_string)
        
        random_string = generate_random_string(50, "adccas%0||<>*-")
        self.assert_alphabet_use("adccas%0||<>*-", random_string)
        
        random_string = generate_random_string(1000, "adccaadsja()/4322!!s%0||<>*-")
        self.assert_alphabet_use("adccaadsja()/4322!!s%0||<>*-", random_string)
   
    def test_should_return_no_alphabet(self):
        random_string = generate_random_string(5, "")
        self.assertEqual(random_string, None)
        
        
    def assert_alphabet_use(self, alphabet: str, string_value: str):
        for i in string_value:
            self.assertIn(i, alphabet)
        
    
if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RandomStringTestClass))


# In[45]:


import unittest

class RandomIDTestClass(unittest.TestCase):
    
    def test_should_return_empty_id(self):
        random_id = create_random_id(0, 1, 2)
        self.assertEqual(0, len(random_id))
        
    def test_should_return_min_result(self):
        random_id = create_random_id(10, 1, 2)
        self.assertEqual(2, len(random_id))
        
    def test_should_return_non_repeated(self):
        random_id = create_random_id(10, 1, 200)
        self.assert_non_repeated(random_id ,1, 200)
    
    def assert_non_repeated(self, ID, minimum, maximum):
        for i in ID:
            self.assertEqual(ID.count(i), 1)
            self.assertTrue(minimum <= int(i) <= maximum)
    
    
if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RandomIDTestClass))


# In[46]:


import unittest

class RandomDateTestClass(unittest.TestCase):
    
    def test_should_return_empty_id(self):
        random_date = generate_random_date()
        self.assert_validate_date(random_date)
        
        random_date = generate_random_date()
        self.assert_validate_date(random_date)
        
        random_date = generate_random_date()
        self.assert_validate_date(random_date)
        
        random_date = generate_random_date()
        self.assert_validate_date(random_date)
        
    def assert_validate_date(self, date):
        date_values = date.split("/")
        self.assertEqual(3, len(date_values))
        self.assertTrue(1 <= int(date_values[0]) <= 31)
        self.assertTrue(1 <= int(date_values[1]) <= 12)
        self.assertTrue(2000 <= int(date_values[2]) <= 2030)

    
if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RandomDateTestClass))


# In[47]:


import unittest

class RandomAddressTestClass(unittest.TestCase):
    
    def test_should_return_address(self):
        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)
        
        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)
        
        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)
        
        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)
        
        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)
        
        random_address = create_random_address()
        self.assertNotEqual(None, random_address)        
        self.assert_address(random_address)
        
        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)
        
        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)
        
        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)
        
        random_address = create_random_address()
        self.assertNotEqual(None, random_address)
        self.assert_address(random_address)
        
    def assert_address(self, address):
        self.assertTrue(
                        "Calle" in address
                        or "Carrera" in address
                        or "Diagonal" in address
                        or "Transversal" in address
                       )

    
if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RandomAddressTestClass))


# In[48]:


import unittest

class RandomWordDictionaryTestClass(unittest.TestCase):
    
    def test_should_return_word(self):
        random_word = choose_random_from_file("dict/test_dict.txt")
        self.assertNotEqual(None, random_word)
        self.assert_word_existence(random_word, "dict/test_dict.txt")
        
        random_word = choose_random_from_file("dict/test_dict.txt")
        self.assertNotEqual(None, random_word)
        self.assert_word_existence(random_word, "dict/test_dict.txt")
        
        random_word = choose_random_from_file("dict/test_dict.txt")
        self.assertNotEqual(None, random_word)
        self.assert_word_existence(random_word, "dict/test_dict.txt")
        
        random_word = choose_random_from_file("dict/test_dict.txt")
        self.assertNotEqual(None, random_word)
        self.assert_word_existence(random_word, "dict/test_dict.txt")
        
        random_word = choose_random_from_file("dict/test_dict.txt")
        self.assertNotEqual(None, random_word)
        self.assert_word_existence(random_word, "dict/test_dict.txt")
    
    def assert_word_existence(self, word, file_name):
        file = open(file_name, "r")
        exists = False
        
        for line in file.readlines():
            exists =  exists or word in line
        self.assertTrue(exists)
        file.close()
    
    
if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RandomWordDictionaryTestClass))


# In[ ]:




