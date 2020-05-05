# coding: utf-8


class MySeq:
    def __getitem__(self, index):
        return index


if __name__ == '__main__':
    s = MySeq()
    print(s[1], type(s[1]))
    print(s[1:4], type(s[1:4]))
    print(s[1:4:2], type(s[1:4:2]))
    print(s[1:4:2, 7:9], type(s[1:4:2, 7:9]))
