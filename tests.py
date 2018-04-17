import unittest
import serverify


class Tests(unittest.TestCase):

    def test_main(self):
        args = serverify.parser.parse_args([
            '-o', '/tmp/serverify-output.txt',
            '-d', '/tmp/serverify-download',
            'test.txt',
        ])
        serverify.main(args=args)

        with open('/tmp/serverify-output.txt', 'r') as fp:
            out = fp.read()

        self.assertTrue(out.startswith('abc==1.2.3'))
        self.assertTrue(out.endswith(
            '/tmp/serverify-download/serverify-pip/\n'))


if __name__ == '__main__':
    unittest.main()
