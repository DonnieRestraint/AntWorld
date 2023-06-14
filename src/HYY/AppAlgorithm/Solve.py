import re
import sys
from functools import reduce

from cryptography.fernet import Fernet
import base64
import os


class Solve(object):

    def __init__(self):
        self.sep = "0001100111"
        self.file_sep = "   "
        self.file_seq_regex = " {3}"
        self.yyh = "YYH"

    def map_table(self):
        table = [
            ('A', '01'),
            ('B', '1000'),
            ('C', '1010'),
            ('D', '100'),
            ('E', '0'),
            ('F', '0010'),
            ('G', '110'),
            ('H', '0000'),
            ('I', '00'),
            ('J', '0111'),
            ('K', '101'),
            ('L', '0100'),
            ('M', '11'),
            ('N', '10'),
            ('O', '111'),
            ('P', '0110'),
            ('Q', '1101'),
            ('R', '010'),
            ('S', '000'),
            ('T', '1'),
            ('U', '001'),
            ('V', '0001'),
            ('W', '011'),
            ('X', '1001'),
            ('Y', '1011'),
            ('Z', '1100'),

            ('0', '11111'),
            ('1', '01111'),
            ('2', '00111'),
            ('3', '00011'),
            ('4', '00001'),
            ('5', '00000'),
            ('6', '10000'),
            ('7', '11000'),
            ('8', '11100'),
            ('9', '11110'),

            ('.', '010101'),
            (':', '111000'),
            (',', '110011'),
            (';', '101010'),
            ('?', '001100'),
            ('=', '10001'),
            ("'", '011110'),
            ('/', '10010'),
            ('!', '101011'),
            ('-', '100001'),
            ('_ ', '001101'),
            ('"', '010010'),
            ('(', '10110'),
            (')', '101101'),
            ('$', '0001001'),
            ('&', '0000'),
            ('@', '011010')
            ]
        return table

    def get_salt(self, salt):
        if type(salt) == str:
            salt = salt + "".join([self.yyh]*11)
            salt = salt[:32]
            salt = base64.urlsafe_b64encode(salt.encode())
            return salt
        else:
            return salt

    def encode(self, salt, pwd):
        password = Fernet(salt).encrypt(pwd.encode()).decode()
        return password

    def decode(self, salt, pwd):
        password = Fernet(salt).decrypt(pwd.encode()).decode()
        return password

    def get_file_data(self, file_path):
        with open(file_path, 'r', encoding="utf-8") as f:
            file_data = f.read()
        return file_data

    def set_file_data(self, file_path, data, mode="a"):
        with open(file_path, mode, encoding="utf-8") as f:
            f.write(data)

    def file_to_encode(self, data, salt):
        data_list = data.split("\n")
        data_list = [_ for rl in data_list for _ in rl.split(" ") if _]
        table_dict = dict(self.map_table()[:-2])
        salt = self.get_salt(salt)
        new_infos = []
        for info in map(lambda info:self.encode(salt, info), data_list):
            ms = []
            for c in info:
                tmp = ''
                for _ in str(ord(c)):
                    if _ in table_dict:
                        tmp += table_dict[_]
                    else:
                        raise ValueError("value error")
                ms.append(tmp)
            new_infos.append(" ".join(ms) + " " + self.sep)
        return " ".join(new_infos)

    def file_to_decode(self, data, salt):
        data_list = [d for d in data.split(" ") if d]
        table_dict = [[t[1], t[0]] for t in self.map_table()[:-2]]
        table_dict = dict(table_dict)
        salt = self.get_salt(salt)
        infos = []
        tmp = []
        for info in data_list:
            if info != self.sep:
                tmp.append(info)
            else:
                infos.append(tmp)
                tmp = []
        new_infos = []
        for info in infos:
            tmp_list = []
            for cs in info:
                c_list = re.findall('.{5}', cs)
                tmp = ''
                for c in c_list:
                    if len(c) != 5:
                        raise ValueError("value error")
                    if c in table_dict:
                        tmp += table_dict[c]
                tmp_list.append(chr(int(tmp)))
            new_infos.append(self.decode(salt, ''.join(tmp_list)))
        name = new_infos[::3]
        user = new_infos[1:][::3]
        acc = new_infos[2:][::3]
        decode_data = []
        for n, u, a in zip(name, user, acc):
            # print(n, u, a)
            decode_data.append((n, u, a))
        return decode_data

    def map_decode(self, data, salt):
        data_list = re.split(self.file_seq_regex, data)
        info = []
        for dt in data_list:
            info.extend(self.file_to_decode(dt, salt))
        return info

    def map_encode(self, data_list, salt):
        sep = self.file_sep
        return reduce(lambda x1, x2: self.file_to_encode(x1, salt) + sep + self.file_to_encode(x2, salt), data_list)

    def map_data(self, data_list):
        sep = self.file_sep
        return reduce(lambda x1, x2: x1 + sep + x2, data_list)

    def check_file(self, file_path):
        file_data = self.get_file_data(file_path)
        return self.check_data(file_data)

    def check_data(self, file_data):
        """
        :return False when code is not encoded
        """
        data = set(file_data)
        if len(data) == 3 and ("1" in data or "0" in data):
            return True
        else:
            return False

    def check_file_salt(self, file_path, salt):
        file_data = self.get_file_data(file_path)
        self.check_data_salt(file_data, salt)

    def check_data_salt(self, file_data, salt):
        """
       :return False when salt is not match file data
        """
        rl = self.check_data(file_data)
        if rl:
            try:
                self.map_decode(file_data, salt)
                return True
            except Exception as err:

                return False
        else:
            return True

    def solve(self):
        if len(sys.argv) > 1:
            path = sys.argv[1]
            try:
                salt = input("input salt:")
                salt2 = input("input salt:")
                if salt2 != salt:
                    print("Inconsistent ~")
                    return
                data = self.get_file_data(path)

                if len(set(data)) == 3 and ("1" in set(data) or "0" in set(data)):
                    self.file_to_decode(data, salt)
                else:
                    new_path = os.path.join(os.path.dirname(path), self.yyh + os.path.basename(path))

                    if os.path.exists(new_path):
                        print(new_path)
                        raise FileExistsError('file exist!')

                    self.set_file_data(new_path, self.file_to_encode(data, salt))
                return 0
            except Exception as err:
                return print(err)


if __name__ == '__main__':
    sys.argv.append(r"C:\Users\F1237055\Desktop\zz\YYHming2wen1234.txt")
    sl = Solve()
    sl.solve()
