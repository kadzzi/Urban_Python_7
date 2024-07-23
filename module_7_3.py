class WordsFinder:
    __NOISE = [',', '.', '=', '!', '?', ';', ':']

    def __init__(self, *file_names):
        self.file_names = file_names

    def string_splitter(self, some_string):
        some_string = some_string.lower().replace('\n', ' ').replace(' - ', ' ')
        result = []
        for char in self.__NOISE:
            some_string = some_string.replace(char, '')
        result.extend([x.strip() for x in some_string.split()])
        return result

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                raw_text = file.read()
            all_words[file_name] = self.string_splitter(raw_text)
        return all_words

    def find(self, word):
        search_result = {}
        for k, v in self.get_all_words().items():
            if word.lower() in v:
                search_result[k] = v.index(word.lower()) + 1
        return search_result

    def count(self, word):
        count_result = {}
        for k, v in self.get_all_words().items():
            if word.lower() in v:
                count_result[k] = v.count(word.lower())
        return count_result


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
