import unittest
import serverify


class Tests(unittest.TestCase):

    def test_main(self):
        with open('/tmp/serverify-requirements.txt', 'w+') as fp:
            fp.write('abc==1.2.3 --hash=sha256:123\n')

        args = serverify.parser.parse_args([
            '-o', '/tmp/serverify-output.txt',
            '-d', '/tmp/serverify-download',
            '/tmp/serverify-requirements.txt',
        ])
        serverify.main(args=args)

        with open('/tmp/serverify-output.txt', 'r') as fp:
            out = fp.read()

        self.assertTrue(out.startswith('abc==1.2.3'))


if __name__ == '__main__':
    unittest.main()
