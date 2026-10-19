import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import check_docs


class DocsTests(unittest.TestCase):
    def test_no_broken_links(self):
        self.assertEqual(check_docs.check_links(), [])

    def test_every_page_has_title(self):
        self.assertEqual(check_docs.check_titles(), [])

    def test_nav_points_to_existing_pages(self):
        self.assertEqual(check_docs.check_nav(), [])

    def test_cli_exit_code(self):
        self.assertEqual(check_docs.main([]), 0)


if __name__ == "__main__":
    unittest.main()
