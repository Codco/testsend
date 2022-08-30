import json
import os
import unittest
import app


def update():
    currentpath = str(os.path.dirname(os.path.abspath(__file__)))
    filedirectories = os.path.join(currentpath, 'fixtures/directories.json')
    filedocuments = os.path.join(currentpath, 'fixtures/documents.json')
    with open(filedocuments, 'r') as out_docs:
        documents = json.load(out_docs)
    with open(filedirectories, 'r') as out_dirs:
        directories = json.load(out_dirs)
    return directories, documents


class Test1(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def testname(self):
        self.assertEqual(app.get_doc_owner_name('2207 876234'), 'Василий Гупкин')

    def testadd(self):
        self.assertEqual(app.add_new_doc('7311', 'pass', 'Shamil', 2), 2)

    def testdelete(self):
        self.assertTrue(app.delete_doc('10006'))


if __name__ == '__main__':
    unittest.main()


class TestYaApi(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def testcreatefolder(self):
        self.assertEqual(user_service.create_folder('test'), 201)

    def testpassed(self):
        self.assertEqual(user_service.create_folder('test_passed'), 409)

    def tearDown(self):
        user_service.delete_folder('test')
        print('method tearDown')


if __name__ == '__main__':
    unittest.main()
